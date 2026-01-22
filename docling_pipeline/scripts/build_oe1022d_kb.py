
import json
import re
import sys
import argparse
from pathlib import Path
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
    if "prov" in item and item["prov"]:
        return item["prov"][0]["page_no"]
    return None

def clean_text(text):
    if not text: return ""
    return text.replace('\n', ' ').strip()

def render_table(table_data):
    """Renders a clean markdown table with vertical deduplication logic."""
    cells = table_data.get("data", {}).get("table_cells", [])
    if not cells: return ""

    # 1. Determine Grid Dimensions
    max_row = 0
    max_col = 0
    for cell in cells:
        max_row = max(max_row, cell["end_row_offset_idx"])
        max_col = max(max_col, cell["end_col_offset_idx"])
    
    # 2. Build Grid
    grid = [["" for _ in range(max_col)] for _ in range(max_row)]
    
    for cell in cells:
        text = clean_text(cell.get("text", ""))
        r = cell["start_row_offset_idx"]
        c = cell["start_col_offset_idx"]
        if r < max_row and c < max_col:
            grid[r][c] = text

    # 3. Apply Vertical Deduplication (Focus on Col 0 for Commands)
    for r in range(1, max_row):
        # Case: Exact match with row above (common in Docling merged cell errors)
        if grid[r][0] == grid[r-1][0] and grid[r][0].strip():
             grid[r][0] = "" 

    # 4. Render Markdown
    lines = []
    # Header
    header = grid[0]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "|".join(["---"] * max_col) + "|")
    # Body
    for row in grid[1:]:
        lines.append("| " + " | ".join(row) + " |")
        
    return "\n".join(lines)

def build_knowledge_base(json_path, output_dir):
    json_path = Path(json_path)
    output_dir = Path(output_dir)
    chapters_dir = output_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Loading {json_path}...")
    with open(json_path, 'r') as f:
        doc = json.load(f)
        
    body_refs = doc.get("body", {}).get("children", [])
    
    # State tracking
    current_chapter_title = "00_Front_Matter"
    current_chapter_lines = []
    current_page = -1
    chapter_index = 0
    
    structure_index = []

    def flush_chapter():
        nonlocal chapter_index, current_chapter_lines, current_chapter_title
        if not current_chapter_lines: return
        
        # Format Filename
        safe_title = re.sub(r'[^\w\s-]', '', current_chapter_title).strip().replace(' ', '_')
        if not safe_title: safe_title = f"Section_{chapter_index}"
        filename = f"{safe_title}.md"
        
        # Subdirectory for Chapter to keep it clean like SMB100A?
        # SMB100A used: chapters/Title/Sec_Title.md
        # Let's stick to flat or single folder for simplicity unless requested:
        # User requested: like SMB100A.
        # SMB100A structure: `chapters/Specific Title/Sec_Specific Title.md`
        
        chapter_subdir = chapters_dir / safe_title
        chapter_subdir.mkdir(exist_ok=True)
        file_path = chapter_subdir / filename
        
        relative_path = f"chapters/{safe_title}/{filename}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(current_chapter_lines))
            
        structure_index.append({
            "title": current_chapter_title,
            "file": relative_path,
            "type": "section",
            "level": 1 # Simplified level
        })
        
        logger.info(f"Saved chapter: {relative_path}")
        
        chapter_index += 1
        current_chapter_lines = []

    logger.info("Processing content...")
    
    for ref in body_refs:
        item = resolve_ref(doc, ref)
        if not item: continue
        
        # Page Marker
        page = get_page_no(item)
        if page and page != current_page:
            current_chapter_lines.append(f"\n<!-- Page {page} -->\n")
            current_page = page
            
        label = item.get("label", "text")
        text = item.get("text", "").strip()
        
        # --- Splitting Logic ---
        # Split on 'section_header' (H1/H2) or 'title'
        # Docling label 'section_header' is usually reliable for headers.
        is_header = label in ["title", "section_header"]
        
        # If header, start new chapter (unless it's very short/empty)
        if is_header and text and len(text) < 100:
            flush_chapter()
            current_chapter_title = text
            # Add header to new file
            current_chapter_lines.append(f"## {text}\n")
            continue
            
        # --- Rendering Logic ---
        if label == "table":
            current_chapter_lines.append(render_table(item))
            current_chapter_lines.append("")
        elif label == "picture":
             current_chapter_lines.append("\n<!-- image -->\n")
        elif label == "list_item":
             current_chapter_lines.append(f"- {text}")
        elif label == "caption":
             current_chapter_lines.append(f"\n*{text}*\n")
        elif text:
             current_chapter_lines.append(f"{text}\n")
             
    # Flush last chapter
    flush_chapter()
    
    # Write Index
    index_path = output_dir / "index.json"
    index_data = {
        "meta": {
            "source": json_path.name,
            "pdf_version": "OE1022D Manual"
        },
        "structure": structure_index
    }
    
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
        
    logger.info(f"Knowledge Base built at: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", help="Path to Docling JSON")
    parser.add_argument("output_dir", help="Target knowledge base directory")
    args = parser.parse_args()
    
    build_knowledge_base(args.input_json, args.output_dir)
