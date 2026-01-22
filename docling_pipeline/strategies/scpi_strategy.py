import re
from typing import Dict, Any, List
from .base_strategy import KnowledgeStrategy

class ScpiStrategy(KnowledgeStrategy):
    def __init__(self, config: Dict):
        super().__init__(config)
        pattern_str = config.get("command_pattern", ".*")
        self.pattern = re.compile(pattern_str)
        self.subheaders = [s.lower() for s in config.get("subheader_keywords", [])]

    def identify_command(self, item: Any, context: Dict) -> bool:
        # SCPI identification is primarily based on Section Headers matching the regex
        from docling_core.types.doc import SectionHeaderItem
        if not isinstance(item, SectionHeaderItem):
            return False
            
        title = getattr(item, 'text', '').strip()
        # Check first word or full title
        first_word = title.split(' ')[0]
        return bool(self.pattern.match(first_word))

    def get_command_name(self, item: Any) -> str:
        title = getattr(item, 'text', '').strip()
        # Return the first word as the command key (e.g. :SOURce:FREQ)
        # But we probably want the full clean title for the filename
        return title

    def is_subheader(self, text: str, level: int) -> bool:
        # Logic from V2: explicit keywords or deeper levels
        clean_text = text.lower().strip().rstrip(':')
        if clean_text in self.subheaders:
            return True
        return False
