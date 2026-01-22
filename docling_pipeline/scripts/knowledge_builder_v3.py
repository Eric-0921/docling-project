
import json
import logging
import re
import shutil
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
from docling_core.types.doc import DoclingDocument, SectionHeaderItem, TextItem, ListItem, GroupItem, TableItem, PictureItem
from ..strategies import create_strategy

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class KnowledgeBuilderV3:
    def __init__(self, input_json_path: Path, output_dir: Path, config_path: Path):
        self.input_json_path = input_json_path
        self.output_dir = output_dir
        self.doc: Optional[DoclingDocument] = None
        
        # Load Config & Strategy
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.strategy = create_strategy(self.config)
        
        self.index_data = {
            "meta": {"device": self.config.get("device_name")},
            "structure": [],
            "command_index": {}
        }
        
        # State Machine context
        self.current_chapter_dir: Optional[Path] = None
        self.current_file_path: Optional[Path] = None
        self.current_content_buffer: List[str] = []
        self.current_is_command_block = False

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
        if not self.doc.body:
            return
        self._process_nodes_linear(self.doc.body.children, chapters_root)
        self._flush_buffer()

    def _process_nodes_linear(self, nodes: List[Any], root_dir: Path):
        for node_ref in nodes:
            item = self._resolve_item(node_ref)
            if not item:
                continue

            # Handle Groups recursively
            label = getattr(item, 'label', '')
            if isinstance(item, GroupItem) or label == 'group':
                children = getattr(item, 'children', [])
                self._process_nodes_linear(children, root_dir)
                continue

            # Handle Content
            self._handle_content_item(item, root_dir)

    def _handle_content_item(self, item, root_dir: Path):
        context = {"current_block": self.current_is_command_block}
        
        # Check if item triggers a new command block
        is_command = self.strategy.identify_command(item, context)
        
        # Check standard headers
        is_header = isinstance(item, SectionHeaderItem)
        title = getattr(item, 'text', '').strip()
        level = getattr(item, 'level', 1)

        # Decision Logic
        if is_header:
            # If it's a subheader of current command, treat as content
            if self.current_is_command_block and self.strategy.is_subheader(title, level):
                self.current_content_buffer.append(f"\n## {title}\n")
                return
            
            # If it is a new command or a structural header -> Flush and New File
            self._flush_buffer()
            
            # Setup File Path
            safe_title = re.sub(r'[^\w\-_\. ]', '_', title)[:60].strip()
            
            # Create/Select Chapter Directory
            # For simplicity, Level 1 headers still define chapters if not commands
            # Or if it is a command, it goes into a generic "Commands" chapter or specific category?
            # V2 Logic: Level 1 = Chapter.
            if level == 1:
                chapter_name = f"{safe_title}"
                self.current_chapter_dir = root_dir / chapter_name
                self.current_chapter_dir.mkdir(exist_ok=True)
            
            if not self.current_chapter_dir:
                self.current_chapter_dir = root_dir / "General"
                self.current_chapter_dir.mkdir(exist_ok=True)

            prefix = "CMD_" if is_command else "Sec_"
            filename = f"{prefix}{safe_title}.md"
            self.current_file_path = self.current_chapter_dir / filename
            
            self.current_content_buffer = [f"# {title}\n"]
            self.current_is_command_block = is_command
            
            # Indexing
            entry = {
                "title": title,
                "file": str(self.current_file_path.relative_to(self.output_dir)),
                "type": "command" if is_command else "section",
                "level": level
            }
            if is_command:
                cmd_key = self.strategy.get_command_name(item)
                self.index_data['command_index'][cmd_key] = entry
            self.index_data['structure'].append(entry)
            
            return

        # Content Items
        if self.current_content_buffer is None:
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
            # Apply Strategy Hook
            final_content = self.strategy.post_process_content(self.current_content_buffer)
            with open(self.current_file_path, "w", encoding="utf-8") as f:
                f.write("".join(final_content))
            self.current_content_buffer = []
            
    def _render_markdown(self, item) -> str:
        if hasattr(item, 'export_to_markdown'):
             try: return item.export_to_markdown()
             except: pass
        
        label = getattr(item, 'label', '')
        text = getattr(item, 'text', '')
        
        if isinstance(item, TextItem) or label == 'text': return f"{text}\n"
        elif isinstance(item, ListItem) or label == 'list_item': return f"- {text}\n"
        elif isinstance(item, TableItem) or label == 'table': return f"\n```table\n{text}\n```\n"
        elif isinstance(item, PictureItem) or label == 'picture': return f"![Picture]({getattr(item, 'self_ref', 'image')})\n"
        return text

    def _resolve_item(self, item_or_ref):
        if not hasattr(item_or_ref, 'cref'): return item_or_ref
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
    parser.add_argument("--output", "-o", type=Path, default=Path("output_kb"))
    parser.add_argument("--config", "-c", type=Path, required=True, help="Path to device config yaml")
    args = parser.parse_args()
    
    builder = KnowledgeBuilderV3(args.input, args.output, args.config)
    builder.build()
