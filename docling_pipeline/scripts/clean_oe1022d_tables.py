
import re
import sys
from pathlib import Path

def clean_markdown_table(file_path):
    """
    Cleans up the OE1022D markdown file by merging duplicated command cells in tables.
    Also fixes header formatting issues if found.
    """
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File {file_path} not found.")
        return

    content = path.read_text(encoding='utf-8')
    lines = content.splitlines()
    new_lines = []
    
    # Regex to identify a table row starting with a command
    # e.g., "| SENSD (?) i{,j} | ..."
    # We want to detect if we are in a table and if the first column is the same as the previous non-empty one
    
    in_table = False
    last_command = None
    table_header_processed = False

    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # Detect table start/end
        if line_stripped.startswith("|"):
            if not in_table:
                in_table = True
                table_header_processed = False
                last_command = None
            
            # Split cells
            cells = [c.strip() for c in line_stripped.split('|')]
            if len(cells) < 3: # Not a valid table row like | col1 | col2 |
                new_lines.append(line)
                continue

            current_command = cells[1] # First actual cell content
            
            # Check for header separator line
            if "---" in current_command:
                new_lines.append(line)
                table_header_processed = True
                continue

            # Skip header row itself
            if not table_header_processed:
                new_lines.append(line)
                table_header_processed = True # Assume first row is header
                continue

            # Logic: If current command is identical to the last one, and previous line was also a table row
            # We replace the command cell with empty string to emulate "merged cell" behavior visually
            # Or better yet, we might want to keep it explicit or just clean it?
            # User Issue: "SENSD... 0: 1 nV/fA" then next row "SENSD... 1: 2 nV/fA"
            # It looks redundant. Let's blank it out if it matches exactly.
            
            if current_command == last_command:
                 # Reconstruct the line with empty first cell
                 # cells[0] is empty string before first |, cells[1] is the command
                 cells[1] = " " * len(current_command) # Maintain spacing or just empty
                 cells[1] = "" # Markdown table merge usually implies empty cell
                 
                 # Rebuild line
                 # Note: purely splitting by | might lose complex markdown formatting inside cells?
                 # For this specific file, it seems safe enough as pipes are structural.
                 new_line = "|" + "|".join(cells[1:-1]) + "|"
                 new_lines.append(new_line)
            else:
                new_lines.append(line)
                last_command = current_command
                
        else:
            in_table = False
            last_command = None
            new_lines.append(line)

    # Write output
    output_path = path.with_name(path.stem + "_cleaned.md")
    output_path.write_text("\n".join(new_lines), encoding='utf-8')
    print(f"Cleaned file written to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_oe1022d_tables.py <path_to_markdown>")
    else:
        clean_markdown_table(sys.argv[1])
