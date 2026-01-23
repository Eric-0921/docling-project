import re

class SCPIGuard:
    def __init__(self):
        self.placeholders = {}
        self.counter = 0
        # Generic pattern for code blocks
        self.code_block_pattern = re.compile(r'(```[\s\S]*?```)')
        # Pattern for inline code that looks like SCPI or technical variables
        # Matches `...` content
        self.inline_code_pattern = re.compile(r'(`[^`]+`)')
        
    def _generate_placeholder(self):
        self.counter += 1
        return f"{{{{CODE_{self.counter:03d}}}}}"

    def protect(self, text):
        """
        Replaces code blocks and sensitive inline code with placeholders.
        Returns the protected text.
        """
        self.placeholders = {}
        self.counter = 0
        protected_text = text

        # 1. Protect Code Blocks (```...```) - Priority 1
        def replace_block(match):
            ph = self._generate_placeholder()
            self.placeholders[ph] = match.group(1)
            return ph

        protected_text = self.code_block_pattern.sub(replace_block, protected_text)

        # 2. Protect Inline Code (`...`) - Priority 2
        # Only protect if it looks "technical" (all caps, numbers, special chars)
        # or if we just decide to protect ALL inline code to be safe.
        # For technical docs, protecting ALL `...` is usually safer.
        protected_text = self.inline_code_pattern.sub(replace_block, protected_text)

        return protected_text

    def restore(self, text):
        """
        Restores placeholders to their original content.
        """
        restored_text = text
        # sort placeholders by length descending to avoid partial replacements (though unlikely with this format)
        for ph, content in self.placeholders.items():
            restored_text = restored_text.replace(ph, content)
        
        return restored_text
