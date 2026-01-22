from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Any
from docling_core.types.doc import DoclingDocument, SectionHeaderItem

class KnowledgeStrategy(ABC):
    def __init__(self, config: Dict):
        self.config = config
        
    @abstractmethod
    def identify_command(self, item: Any, context: Dict) -> bool:
        """
        Determines if a document item represents the start of a command block.
        """
        pass

    @abstractmethod
    def get_command_name(self, item: Any) -> str:
        """
        Extracts the command name from the item.
        """
        pass

    @abstractmethod
    def is_subheader(self, text: str, level: int) -> bool:
        """
        Determines if a header is a child of the current command block.
        """
        pass
        
    @abstractmethod
    def post_process_content(self, content_buffer: List[str]) -> List[str]:
        """
        Optional hook to clean up or format Markdown content before saving.
        """
        return content_buffer
