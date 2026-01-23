class MarkdownParser:
    def __init__(self, max_chars=1500):
        self.max_chars = max_chars

    def parse_and_chunk(self, content):
        """
        Splits markdown content into chunks based on headings and size limits.
        Refined to respect paragraph boundaries.
        """
        lines = content.split('\n')
        chunks = []
        current_chunk = []
        current_char_count = 0
        
        for line in lines:
            line_len = len(line) + 1 # count newline
            
            # Heuristic trigger for splitting:
            # 1. Start of a new level 1 or 2 header
            # 2. Current chunk is substantially large
            is_major_header = line.strip().startswith('# ') or line.strip().startswith('## ')
            
            if (is_major_header and current_char_count > 100) or (current_char_count + line_len > self.max_chars):
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = []
                    current_char_count = 0

            current_chunk.append(line)
            current_char_count += line_len

        if current_chunk:
            chunks.append('\n'.join(current_chunk))

        return chunks
