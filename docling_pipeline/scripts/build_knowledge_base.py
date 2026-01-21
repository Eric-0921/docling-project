
import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from docling_core.types.doc import DoclingDocument, SectionHeaderItem, TextItem, ListItem, GroupItem

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Allow mixed case (e.g. :SOURce), <brackets>, and multiple segments
SCPI_PATTERN = re.compile(r"^:?[a-zA-Z]{2,}(:[a-zA-Z0-9_]+)*(\<.*\>)?(:[a-zA-Z0-9_]+)*(\?)?$")

class KnowledgeBaseBuilder:
    def __init__(self, input_json_path: Path, output_dir: Path):
        self.input_json_path = input_json_path
        self.output_dir = output_dir
        self.doc: Optional[DoclingDocument] = None
        self.index_data = {
            "meta": {},
            "structure": [],
            "scpi_index": {}
        }

    def load_document(self):
        logger.info(f"Loading JSON from {self.input_json_path}...")
        with open(self.input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # DoclingDocument.model_validate behaves differently depending on version
        # Some versions might need conversion from dict
        try:
            self.doc = DoclingDocument.model_validate(data)
        except Exception as e:
            logger.error(f"Failed to validate DoclingDocument: {e}")
            raise e
        
        logger.info("Document loaded successfully.")

    def build(self):
        self.load_document()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. Extract Meta
        self._extract_metadata()
        
        # 2. Build Hierarchy & SCPI Index
        self._traverse_document()
        
        # 3. Save Index
        self._save_index()
        
        logger.info("Knowledge Base Build Complete.")

    def _extract_metadata(self):
        self.index_data["meta"] = {
            "name": self.doc.name or self.input_json_path.stem,
            "origin": self.doc.origin.filename if self.doc.origin else "unknown"
        }
        # In future: parse confidence scores if available in specific field

    def _traverse_document(self):
        """
        Traverse the document body to build the knowledge tree.
        We expect a hierarchical structure in self.doc.body.children
        """
        if not self.doc.body:
            logger.warning("Document has no body!")
            return

        # Start recursion from root children
        self.index_data["structure"] = self._process_children(self.doc.body.children)

    def _process_children(self, children: List[Any], level: int = 1) -> List[Dict]:
        nodes = []
        
        current_section = None
        
        for child_ref in children:
            item = self._resolve_item(child_ref)
            if not item:
                continue

            # Check type of item
            # Docling Core types might be Pydantic models, so use isinstance or check attributes
            
            # Label check is robust
            label = getattr(item, 'label', '')
            
            if isinstance(item, SectionHeaderItem) or label == 'section_header':
                # New Section Found
                title = item.text.strip() if hasattr(item, 'text') else ""
                
                # Check for SCPI Command
                if SCPI_PATTERN.match(title.split(' ')[0]): # Check first word for SCPI
                   self._register_scpi_command(title, item)
                   
                node = {
                    "title": title,
                    "level": item.level if hasattr(item, 'level') else level,
                    "type": "section",
                    "text_preview": title[:50]
                }
                nodes.append(node)
                current_section = node
                
            elif isinstance(item, GroupItem) or label == 'group':
                # It's a group
                children_list = getattr(item, 'children', [])
                group_children = self._process_children(children_list, level + 1)
                
                group_node = {
                    "type": "group",
                    "children": group_children
                }
                
                # Heuristic: if group starts with a section, merge info
                if group_children and group_children[0].get('type') == 'section':
                    head = group_children[0]
                    group_node.update(head)
                    group_node['children'] = group_children[1:]
                
                nodes.append(group_node)
            
            elif isinstance(item, (TextItem, ListItem)) or label in ['text', 'list_item']:
                 text = getattr(item, 'text', '').strip()
                 if ":SOUR" in text and "Example" in text:
                     # Check for inline SCPI candidate
                     pass

        return nodes

    def _resolve_item(self, item_or_ref):
        """
        Resolves a RefItem to the actual object in the document lists.
        """
        # If it's already an item (structurally embedded), return it
        if not hasattr(item_or_ref, 'cref'): 
            return item_or_ref
            
        ref_str = item_or_ref.cref
        if not ref_str.startswith("#/"):
            return item_or_ref

        # Parse reference #/texts/123
        parts = ref_str.split('/')
        if len(parts) < 3:
            return None
        
        collection_name = parts[1] # e.g. 'texts', 'groups', 'tables'
        try:
            index = int(parts[2])
        except ValueError:
            return None
            
        collection = getattr(self.doc, collection_name, [])
        if 0 <= index < len(collection):
            return collection[index]
            
        return None

    def _register_scpi_command(self, command_text: str, item: Any):
        # Normalize command
        cmd = command_text.split(' ')[0] # usage ":SOURce:FREQ 5GHz" -> ":SOURce:FREQ"
        
        entry = {
            "full_text": command_text,
            "prov": item.prov[0].dict() if item.prov else None
        }
        
        self.index_data["scpi_index"][cmd] = entry
        logger.info(f"Registered SCPI Command: {cmd}")

    def _save_index(self):
        out_path = self.output_dir / "index.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(self.index_data, f, indent=2)
        logger.info(f"Saved Index to {out_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--output", "-o", type=Path, default=Path("output_knowledge_base"))
    args = parser.parse_args()
    
    builder = KnowledgeBaseBuilder(args.input, args.output)
    builder.build()
