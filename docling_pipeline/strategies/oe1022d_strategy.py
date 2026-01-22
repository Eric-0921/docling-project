import re
from typing import Dict, Any, List
from .base_strategy import KnowledgeStrategy

class Oe1022dStrategy(KnowledgeStrategy):
    def __init__(self, config: Dict):
        super().__init__(config)
        pattern_str = config.get("command_pattern", ".*")
        self.pattern = re.compile(pattern_str)
        self.subheaders = [s.lower() for s in config.get("subheader_keywords", [])]

    def identify_command(self, item: Any, context: Dict) -> bool:
        from docling_core.types.doc import SectionHeaderItem, TableItem
        
        # 1. Check Section Headers
        if isinstance(item, SectionHeaderItem):
            title = getattr(item, 'text', '').strip()
            # Loose check for command-like headers
            if self.pattern.match(title):
                return True
        
        # 2. Check for Table-driven definitions (Special Feature)
        # Detailed logic to be implemented after prototyping
        # For now, rely on headers if Docling detects them
        
        return False

    def get_command_name(self, item: Any) -> str:
        title = getattr(item, 'text', '').strip()
        return title.split(' ')[0] # E.g. "SENS" from "SENS D"

    def is_subheader(self, text: str, level: int) -> bool:
        clean_text = text.lower().strip().rstrip(':')
        if clean_text in self.subheaders:
            return True
        return False
