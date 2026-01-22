
import json
import sys
from pathlib import Path

def resolve_ref(doc, ref):
    """Resolves a JSON pointer like '#/texts/0' to the actual object."""
    if not isinstance(ref, dict) or "$ref" not in ref:
        return ref
    
    path = ref["$ref"]
    parts = path.lstrip('#/').split('/')
    
    current = doc
    for part in parts:
        if isinstance(current, list):
            current = current[int(part)]
        else:
            current = current.get(part)
    return current

def get_page_no(item):
    """Extracts page number from item provenance."""
    if "prov" in item and item["prov"]:
        return item["prov"][0]["page_no"]
    return None

def clean_text(text):
    """Cleans text for markdown."""
    if not text:
        return ""
    return text.replace('\n', ' ').strip()

def render_table(table_data):
    """Renders a simplified markdown table with vertical deduplication."""
    # Build grid
    grid = table_data.get("grid", []) # Docling JSON usually has grid or cells
    # Check if we have pre-computed grid or need to build from cells
    # Docling v2 JSON usually has 'data' -> 'grid' (list of lists of cells)
    
    # If using 'table_cells', we need to reconstruct.
    # But checking previous output, 'data' had 'table_cells'.
    # Let's handle 'table_cells' to build a simple grid.
    
    cells = table_data.get("data", {}).get("table_cells", [])
    if not cells:
        return ""

    # Determine dimensions
    max_row = 0
    max_col = 0
    for cell in cells:
        max_row = max(max_row, cell["end_row_offset_idx"])
        max_col = max(max_col, cell["end_col_offset_idx"])
    
    # Initialize empty grid
    table_grid = [["" for _ in range(max_col)] for _ in range(max_row)]
    
    # Populate grid
    for cell in cells:
        text = clean_text(cell.get("text", ""))
        r_start = cell["start_row_offset_idx"]
        c_start = cell["start_col_offset_idx"]
        # Basic content fill - ignoring spans for simplification, just filling top-left
        # Or better: verify how Docling outputs text in spans.
        table_grid[r_start][c_start] = text
        
    # LOGIC: Vertical Deduplication (for Command Names in Col 0)
    # And specifically for OE1022D, merge identical cells in Col 0
    for r in range(1, max_row):
        # Check Col 0
        if table_grid[r][0] == table_grid[r-1][0] and table_grid[r][0].strip():
            table_grid[r][0] = "" # Clear it to simulate merge

    # Check Header
    # If Row 0 is extremely long (like a description), maybe it shouldn't be a header?
    # For now, standard markdown: Row 0 is header, Row 1 is separator.
    
    md_lines = []
    
    # Header
    header = table_grid[0]
    md_lines.append("| " + " | ".join(header) + " |")
    
    # Separator
    md_lines.append("|" + "|".join(["---"] * max_col) + "|")
    
    # Body
    for row in table_grid[1:]:
        md_lines.append("| " + " | ".join(row) + " |")
        
    return "\n".join(md_lines)

def generate_markdown(json_path, output_path):
    print(f"Loading {json_path}...")
    with open(json_path, 'r') as f:
        doc = json.load(f)
        
    body_refs = doc.get("body", {}).get("children", [])
    if not body_refs:
        print("No body content found.")
        return

    lines = []
    current_page = -1
    
    print(f"Processing {len(body_refs)} items...")
    
    for ref in body_refs:
        item = resolve_ref(doc, ref)
        if not item:
            continue
            
        # Page Marker
        page = get_page_no(item)
        if page and page != current_page:
            lines.append(f"\n<!-- Page {page} -->\n")
            current_page = page
            
        # Render Item
        label = item.get("label", "text")
        
        if label == "table":
            # Render Table
            table_md = render_table(item)
            lines.append(table_md)
            lines.append("") # Spacer
            
        elif label == "picture":
             lines.append("\n<!-- image -->\n")
             
        elif label in ["text", "paragraph", "title", "section_header", "caption", "list_item"]:
             text = item.get("text", "").strip()
             if not text:
                 continue
                 
             # Simple heuristic for headers based on label or structure
             # Docling usually has specific labels. 'title', 'section_header'
             if label in ["title", "section_header"]:
                 level = 2 # Default to H2
                 # If we had hierarchy info we could do ##, ### etc.
                 # For now, let's guess based on level if available or just use ##
                 lines.append(f"\n## {text}\n")
             elif label == "caption":
                  lines.append(f"\n*{text}*\n")
             elif label == "list_item":
                  lines.append(f"- {text}")
             else:
                  lines.append(f"{text}\n")
                  
    # Write Output
    print(f"Writing to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print("Done!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_structured_md.py <json_file> [output_file]")
        sys.exit(1)
        
    json_file = sys.argv[1]
    if len(sys.argv) > 2:
        out_file = sys.argv[2]
    else:
        out_file = Path(json_file).with_suffix('.md')
        
    generate_markdown(json_file, out_file)
