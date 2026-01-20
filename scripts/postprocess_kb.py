
import json
import re
import argparse
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SCPI_PATTERN = r'^:?[A-Z]{2,}(:[A-Z]{2,})*'

def clean_text(text):
    """Clean common OCR artifacts"""
    if not text: return ""
    # Remove leader dots (e.g., "Chapter 1 .......... 5")
    text = re.split(r'\.{3,}', text)[0]
    return text.strip()

def extract_scpi_commands(tables):
    """Deep analysis of tables to find SCPI commands"""
    scpi_commands = []
    for table in tables:
        data = table.get("data", [])
        if not data: continue
        
        # Simple heuristic: Look for "Command" and "Parameter" in header
        header = [str(c.get("text", "")).lower() if isinstance(c, dict) else str(c).lower() for c in data[0]]
        if "command" in header and "parameter" in header:
            cmd_idx = header.index("command")
            param_idx = header.index("parameter")
            
            for row in data[1:]:
                if len(row) > max(cmd_idx, param_idx):
                    cmd = row[cmd_idx].get("text", "").strip() if isinstance(row[cmd_idx], dict) else str(row[cmd_idx]).strip()
                    param = row[param_idx].get("text", "").strip() if isinstance(row[param_idx], dict) else str(row[param_idx]).strip()
                    
                    if cmd and (':' in cmd or cmd.isupper()):
                        scpi_commands.append({"command": cmd, "parameter": param})
    return scpi_commands

def semantic_split(data, output_dir):
    """Split content into chapters based on H1 headers"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    current_chapter_title = "00_Preamble"
    current_content = []
    chapter_index = 0
    
    # Iterate through texts to find headers
    # Note: Docling's JSON structure puts texts in a flat list often. 
    # We rely on 'type' == 'section_header' and 'level' == 1 if available, 
    # or fallback to visual analysis if needed. Docling v2 usually provides 'level'.
    
    items = data.get("texts", [])
    if not items:
        # Fallback for some Docling versions that might put structure elsewhere
        logger.warning("No text items found in JSON root.")
        return

    for item in items:
        text = item.get("text", "")
        # Check for Level 1 Header
        # Assuming Docling output has 'label' or 'level'. Adjust based on actual JSON schema version.
        # Fallback heuristic: All caps short line, or explicit metadata if available.
        
        is_h1 = False
        if item.get("label") == "section_header" and item.get("level") == 1:
            is_h1 = True
        
        if is_h1:
            # Save previous chapter
            if current_content:
                save_chapter(output_dir, chapter_index, current_chapter_title, current_content)
                chapter_index += 1
                current_content = []
            
            current_chapter_title = clean_text(text).replace(" ", "_").replace("/", "-")
            if len(current_chapter_title) > 50: current_chapter_title = current_chapter_title[:50]
        
        current_content.append(item)
    
    # Save last chapter
    if current_content:
        save_chapter(output_dir, chapter_index, current_chapter_title, current_content)

def save_chapter(output_dir, index, title, items):
    filename = f"{index:02d}_{title}.md"
    path = output_dir / filename
    
    with open(path, "w", encoding="utf-8") as f:
        # Frontmatter
        f.write(f"---\n")
        f.write(f"chapter_index: {index}\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"--- \n\n")
        
        f.write(f"# {title}\n\n")
        
        for item in items:
            text = clean_text(item.get("text", ""))
            if text:
                f.write(f"{text}\n\n")
                
    logger.info(f"Saved chapter: {filename}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", help="Path to Docling raw JSON output")
    args = parser.parse_args()
    
    input_path = Path(args.input_json)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        return

    # Determine Output Directory (Knowledge Base)
    # If input is output/run_ID/raw/file.json
    # We want output/run_ID/knowledge_base/
    run_dir = input_path.parent.parent
    kb_dir = run_dir / "knowledge_base"
    
    logger.info(f"Processing {input_path}")
    logger.info(f"Output target: {kb_dir}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Semantic Splitting
    semantic_split(data, kb_dir)
    
    # 2. SCPI Extraction (Global)
    if "tables" in data:
        scpi_cmds = extract_scpi_commands(data["tables"])
        scpi_path = kb_dir / "scpi_database.json"
        with open(scpi_path, "w", encoding='utf-8') as f:
            json.dump(scpi_cmds, f, indent=2)
        logger.info(f"Extracted {len(scpi_cmds)} SCPI commands to database")

if __name__ == "__main__":
    main()
