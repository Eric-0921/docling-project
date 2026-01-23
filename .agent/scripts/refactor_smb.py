import re
import sys

def refactor(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    
    # Regex patterns
    footer_re = re.compile(r'^\s*(\d+(\.\d+)*\s*\|\s*)?版本\s*\d+\s*\|\s*R&S®\s*SMB.*$') # Matches "1407.0806.32 | 版本 23 | R&S® SMB100A"
    page_num_re = re.compile(r'^\s*\d+\s*$')
    
    # Matches "# 1.2 Title" or "## 1.2 Title"
    header_re = re.compile(r'^(#+)\s*(\d+(\.\d+)*)\s+(.*)$')
    
    # Table header liberation: | 3.1.14 | Title ... |
    # Careful not to match normal table rows that happen to start with a number in first col if they aren't headers.
    # But for this manual, numbered items in tables are usually headers.
    table_header_re = re.compile(r'^\|\s*(\d+(\.\d+)*)\s*\|\s*(.*?)\s*\|.*$')
    
    # Alerts
    alert_header_re = re.compile(r'^#+\s*(警告|注意|小心|Warning|Caution|Advice|Tip)\s*$')
    # Inline alerts: "注意！" or "2. 注意！"
    alert_inline_re = re.compile(r'^(\s*)(\d+\.\s*)?(注意|警告|小心|Warning|Caution)[！!]\s*(.*)$')
    
    image_re = re.compile(r'^\s*(<!--\s*image\s*-->|!\[\]\(.*\))\s*$')
    table_dots_re = re.compile(r'\.{2,}')

    # State
    in_toc = False
    toc_done = False
    in_alert_block = False # To capture next line for alert
    
    iterator = iter(range(len(lines)))
    
    for i in iterator:
        line = lines[i]
        stripped = line.strip()

        # 1. Metadata (rough keep)
        if i < 11: 
            new_lines.append(line)
            continue
            
        # 2. TOC Removal
        # Start of TOC
        if not toc_done and (stripped == "## 目录" or "| 1       | 安全与法规信息" in stripped):
            in_toc = True
            continue # Skip this line
        
        if in_toc:
            # End of TOC detection
            # If we hit a header like "## 1 安全..." or text "安全说明" that is NOT in a table
            if (stripped.startswith("## 1") or stripped == "安全说明") and not stripped.startswith("|"):
                in_toc = False
                toc_done = True
                # Process this line as content
            elif stripped.startswith("## ") and "目录" not in stripped:
                # Detected a header that probably follows TOC
                in_toc = False
                toc_done = True
            else:
                 # Skip TOC line
                 continue
                 
        # 3. Artifact Cleanup
        if footer_re.search(stripped): # Use search to match partial match in line
            continue
        if page_num_re.match(stripped):
            # Ensure it's not a list item "1."
            if re.match(r'^\d+$', stripped):
                continue

        # 4. Structural Liberation (Table Headers)
        t_match = table_header_re.match(stripped)
        if t_match:
            num = t_match.group(1)
            text = t_match.group(3)
            # Clean dots and trailing page nums
            text = table_dots_re.sub('', text)
            text = re.sub(r'\s+\d+\s*$', '', text).strip()
            
            level = num.count('.') + 1
            hashes = '#' * level
            new_lines.append(f"{hashes} {num} {text}\n")
            continue

        # 5. Header Re-leveling
        h_match = header_re.match(stripped)
        if h_match:
            num = h_match.group(2)
            title = h_match.group(4)
            level = num.count('.') + 1
            hashes = '#' * level
            new_lines.append(f"{hashes} {num} {title}\n")
            in_alert_block = False
            continue
            
        # 6. Alerts
        # Case A: Header "## 警告"
        if alert_header_re.match(stripped):
            alert_type = alert_header_re.match(stripped).group(1)
            new_lines.append(f"> ⚠️ **{alert_type}**\n")
            new_lines.append(">\n")
            in_alert_block = True
            continue
            
        # Case B: Inline
        a_match = alert_inline_re.match(line) # Use line to preserve indentation
        if a_match:
            indent = a_match.group(1)
            list_prefix = a_match.group(2) or ""
            atype = a_match.group(3) # 注意
            content = a_match.group(4)
            
            # Format
            if list_prefix:
                # It was "2. 注意！..."
                # Output "2. " then blockquote
                new_lines.append(f"{indent}{list_prefix}\n")
                new_lines.append(f"{indent}   > ⚠️ **{atype}**\n")
                new_lines.append(f"{indent}   >\n")
                new_lines.append(f"{indent}   > {content}\n")
            else:
                new_lines.append(f"> ⚠️ **{atype}**\n")
                new_lines.append(">\n")
                new_lines.append(f"> {content}\n")
            in_alert_block = False # Inline handled immediately
            continue

        # Handle next line of Alert Header block
        if in_alert_block:
            if stripped: # Non empty
                new_lines.append(f"> {stripped}\n")
                in_alert_block = False # Assume single paragraph for now
            else:
                # Empty line, keep block open? or just skip?
                # Usually markdown blockquote needs > on empty lines too
                new_lines.append(">\n") 
            continue

        # 7. Images
        if image_re.match(stripped):
            # Check for duplicate (look back through empty lines)
            is_dup = False
            for prev in reversed(new_lines):
                if not prev.strip():
                    continue
                if "> *[图示" in prev or "<!-- image -->" in prev:
                    is_dup = True
                break # Stop at first non-empty line
            
            if is_dup:
                continue

            # Contextual guess? Hard.
            new_lines.append("> *[图示：此处原文档包含相关操作示意图]*\n")
            continue

        # 8. Table Clean
        if "|" in line:
            # Table row
            cleaned = table_dots_re.sub('', line)
            new_lines.append(cleaned)
            continue

        # Default
        new_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python refactor_smb.py input output")
    else:
        refactor(sys.argv[1], sys.argv[2])
