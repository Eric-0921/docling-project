
import json
import logging
import re
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
from docling_core.types.doc import DoclingDocument, SectionHeaderItem, TextItem, ListItem, GroupItem, TableItem, PictureItem

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# SCPI Pattern: Must start with * OR contain at least one colon (:) for hierarchy
# e.g. *RST, :SOURce:FREQ, SOURce:FREQ
SCPI_PATTERN = re.compile(r"^(\*[a-zA-Z0-9]+.*)|(:?[a-zA-Z0-9_]+:[a-zA-Z0-9_]+.*)$")

class KnowledgeBuilderV2:
    def __init__(self, input_json_path: Path, output_dir: Path):
        self.input_json_path = input_json_path
        self.output_dir = output_dir
        self.doc: Optional[DoclingDocument] = None
        self.index_data = {
            "meta": {},
            "structure": [],
            "scpi_index": {}
        }
        
        # State Machine context
        self.current_chapter_dir: Optional[Path] = None
        self.current_file_path: Optional[Path] = None
        self.current_content_buffer: List[str] = []
        self.current_node_meta: Dict = {} # Title, Level, etc.
        self.current_is_scpi_block = False

    def build(self):
        self._load_document()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize Output Structure
        chapters_dir = self.output_dir / "chapters"
        if chapters_dir.exists():
            shutil.rmtree(chapters_dir)
        chapters_dir.mkdir()

        # Traverse
        self._traverse_document(chapters_dir)
        
        # Save Metadata
        self._save_index()
        logger.info(f"Knowledge Base generated at {self.output_dir}")

    def _load_document(self):
        logger.info(f"Loading JSON from {self.input_json_path}...")
        with open(self.input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        try:
            self.doc = DoclingDocument.model_validate(data)
        except Exception as e:
            logger.error(f"Docling Validation Failed: {e}")
            raise e

    def _traverse_document(self, chapters_root: Path):
        """
        Linear traversal of the document 'body' is preferred for sequential streaming.
        If 'body.children' contains Groups, we flatten them logically or handle recursion.
        """
        if not self.doc.body:
            return
            
        # We process the top-level children. 
        # If they are groups, we dive in.
        self._process_nodes_linear(self.doc.body.children, chapters_root)
        
        # Flush final buffer
        self._flush_buffer()

    def _process_nodes_linear(self, nodes: List[Any], root_dir: Path):
        for node_ref in nodes:
            item = self._resolve_item(node_ref)
            if not item:
                continue

            # Handle Groups recursively (Flattening strategy)
            label = getattr(item, 'label', '')
            if isinstance(item, GroupItem) or label == 'group':
                children = getattr(item, 'children', [])
                self._process_nodes_linear(children, root_dir)
                continue

            # Handle Content Items
            self._handle_content_item(item, root_dir)

    def _handle_content_item(self, item, root_dir: Path):
        label = getattr(item, 'label', '')
        
        # 1. Section Headers (Boundaries)
        if isinstance(item, SectionHeaderItem) or label == 'section_header':
            title = getattr(item, 'text', '').strip()
            level = getattr(item, 'level', 1)
            
            # SCPI Detection
            is_scpi = bool(SCPI_PATTERN.match(title.split(' ')[0]))
            
            # Sub-header Detection logic for SCPI context
            # Common subheaders in SCPI blocks that are detected as Level 1
            is_subheader = title.lower().rstrip(':') in [
                "parameters", "example", "usage", "return values", "manual operation", 
                "options", "setting parameters", "return values", "query"
            ]
            
            # If we are in a SCPI block, certain headers should be treated as children
            if self.current_is_scpi_block:
                if is_subheader or (level > 1 and not is_scpi):
                     # Downgrade to content
                     self.current_content_buffer.append(f"\n## {title}\n")
                     return
            
            # Else, it's a real boundary -> Flush
            self._flush_buffer() 
            
            # Setup new File Path
            safe_title = re.sub(r'[^\w\-_\. ]', '_', title)[:60].strip()
            
            # Directory Management (Simulated by Level 1)
            if level == 1:
                chapter_name = f"{safe_title}"
                self.current_chapter_dir = root_dir / chapter_name
                self.current_chapter_dir.mkdir(exist_ok=True)
            
            if not self.current_chapter_dir:
                self.current_chapter_dir = root_dir / "General"
                self.current_chapter_dir.mkdir(exist_ok=True)

            # Filename
            prefix = "SCPI_" if is_scpi else "Sec_"
            filename = f"{prefix}{safe_title}.md"
            self.current_file_path = self.current_chapter_dir / filename
            
            # Start Buffer
            self.current_content_buffer = [f"# {title}\n"]
            self.current_is_scpi_block = is_scpi # Update State
            
            # Register to Index
            entry = {
                "title": title,
                "file": str(self.current_file_path.relative_to(self.output_dir)),
                "type": "scpi_command" if is_scpi else "section",
                "level": level
            }
            if is_scpi:
                # Use full title or first word? Title is safer e.g. ":SOURce:FREQ"
                cmd_key = title.split(' ')[0]
                self.index_data['scpi_index'][cmd_key] = entry
            self.index_data['structure'].append(entry)
            
            return

        # 2. Content (Text, Table, List, etc.)
        # Append to current buffer
        if self.current_content_buffer is None:
             # Content before first header?
             # Initialize a preamble file
             if not self.current_chapter_dir:
                 self.current_chapter_dir = root_dir / "Preamble"
                 self.current_chapter_dir.mkdir(exist_ok=True)
             self.current_file_path = self.current_chapter_dir / "Introduction.md"
             self.current_content_buffer = ["# Introduction\n"]

        content_md = self._render_markdown(item)
        if content_md:
            self.current_content_buffer.append(content_md + "\n")

    def _flush_buffer(self):
        if self.current_file_path and self.current_content_buffer:
            with open(self.current_file_path, "a", encoding="utf-8") as f: # Append or Write? 
                # Since we traverse linearly, one section = one flush? 
                # No, we flush AT the start of NEXT section.
                # So we should write 'w' initially? 
                # Efficient: collect all in list, write once 'w'.
                f.write("\n".join(self.current_content_buffer))
            
            # Reset
            self.current_content_buffer = []
            self.current_file_path = None # Wait for next header to set path?
            # Actually, if we encounter CONTENT after flushing, it belongs to... whom?
            # It belongs to the PREVIOUS header unless a NEW header appeared.
            # My logic in _handle_content_item says "If Header -> Flush -> Start New".
            # So content always appends to current.

    def _flush_buffer(self):
        """
        Refined flush: write current buffer to current file.
        """
        if self.current_file_path and self.current_content_buffer:
            # Check if file exists to determine mode?
            # Actually, logic: Header triggers NEW file. So we 'w' write.
            # But what if we flush at end of document?
            mode = 'w' 
            # Wait, if I split mainly by Level 1, then Level 2 headers are just content inside Level 1 file?
            # User wants "SCPI Command" to be its own file.
            # SCPI commands are Level 1 in the PDF (based on Demo).
            # So yes, new file per Level 1 is correct.
            # What about Level 2? 
            # If Level 2 appears, does it close Level 1 file? 
            # YES, granular splitting key.
            # So 'w' is safe.
            
            with open(self.current_file_path, "w", encoding="utf-8") as f:
                f.write("".join(self.current_content_buffer))
            self.current_content_buffer = []

    def _render_markdown(self, item) -> str:
        # Try native export first (Table, Text, etc.)
        if hasattr(item, 'export_to_markdown'):
             try:
                 return item.export_to_markdown()
             except Exception:
                 pass # Fallback
                 
        label = getattr(item, 'label', '')
        text = getattr(item, 'text', '')
        
        if isinstance(item, TextItem) or label == 'text':
            return f"{text}\n"
        
        elif isinstance(item, ListItem) or label == 'list_item':
            marker = getattr(item, 'marker', '-')
            return f"{marker} {text}\n"
            
        elif isinstance(item, TableItem) or label == 'table':
             # Fallback if export failed or not available (likely handled above)
             return f"\n```table\n{text}\n```\n"
        
        elif isinstance(item, PictureItem) or label == 'picture':
             return f"![Picture]({getattr(item, 'self_ref', 'image')})\n"
             
        return text

    def _resolve_item(self, item_or_ref):
        # ... logic from V1 ...
        if not hasattr(item_or_ref, 'cref'): 
            return item_or_ref
        ref_str = item_or_ref.cref
        if not ref_str.startswith("#/"): return item_or_ref
        parts = ref_str.split('/')
        if len(parts) < 3: return None
        collection = getattr(self.doc, parts[1], [])
        idx = int(parts[2])
        if 0 <= idx < len(collection): return collection[idx]
        return None

    def _save_index(self):
        out_path = self.output_dir / "index.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(self.index_data, f, indent=2)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--output", "-o", type=Path, default=Path("output_kb_full"))
    args = parser.parse_args()
    
    builder = KnowledgeBuilderV2(args.input, args.output)
    builder.build()
