
import json
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SCPI_PATTERN = r'^:?[A-Z]{2,}(:[A-Z]{2,})*'
LEADER_DOTS_PATTERN = r'\.{3,}\s*\d+'

def clean_toc_title(text):
    """Clean leader dots and page numbers from TOC entries"""
    if not text:
        return ""
    # Remove leader dots and trailing numbers
    text = re.split(r'\.{3,}', text)[0]
    return text.strip()

def extract_scpi_commands(tables):
    """
    Identify and structure SCPI command tables from Docling table output.
    Returns a list of structured command definitions.
    """
    scpi_commands = []
    
    for table in tables:
        data = table.get("data", [])
        if not data:
            continue
            
        # Check header row for SCPI keywords
        headers = [str(h).lower() for h in data[0] if h]
        header_text = " ".join(headers)
        
        # Heuristic 1: Header contains "command" or "parameter"
        if "command" in header_text and ("parameter" in header_text or "remark" in header_text or "unit" in header_text):
            logger.info("Found potential SCPI table")
            
            # Map column indices
            cmd_idx = -1
            param_idx = -1
            unit_idx = -1
            remark_idx = -1
            
            for i, h in enumerate(headers):
                if "command" in h: cmd_idx = i
                elif "parameter" in h: param_idx = i
                elif "unit" in h: unit_idx = i
                elif "remark" in h or "comment" in h: remark_idx = i
            
            if cmd_idx == -1:
                continue
                
            # Iterate rows (skip header)
            for row in data[1:]:
                # Handle row length mismatch
                if len(row) <= cmd_idx:
                    continue
                    
                cmd_raw = row[cmd_idx].get("text", "") if isinstance(row[cmd_idx], dict) else str(row[cmd_idx])
                
                # Heuristic 2: First cell looks like SCPI command
                if ':' in cmd_raw or cmd_raw.isupper():
                    cmd_entry = {
                        "command": cmd_raw.strip(),
                        "parameters": str(row[param_idx]).strip() if param_idx != -1 and len(row) > param_idx else "",
                        "unit": str(row[unit_idx]).strip() if unit_idx != -1 and len(row) > unit_idx else "",
                        "description": str(row[remark_idx]).strip() if remark_idx != -1 and len(row) > remark_idx else ""
                    }
                    scpi_commands.append(cmd_entry)
                    
    return scpi_commands

def postprocess_json(json_path):
    json_path = Path(json_path)
    logger.info(f"Processing: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed_data = {
        "metadata": {"source": str(json_path)},
        "scpi_commands": [],
        "cleaned_text": []
    }

    # Extract SCPI commands from tables
    if "tables" in data:
        commands = extract_scpi_commands(data["tables"])
        processed_data["scpi_commands"].extend(commands)
        logger.info(f"Extracted {len(commands)} SCPI commands")

    # Clean text blocks
    # Logic to separate English commands from descriptive text for translation
    for item in data.get("texts", []):
        text = item.get("text", "")
        if not text:
            continue
            
        # Simple cleanup
        text = clean_toc_title(text)
        
        processed_data["cleaned_text"].append({
            "text": text,
            "type": item.get("type", "text"),
            # Tag SCPI commands for protection
            "is_scpi": bool(re.match(SCPI_PATTERN, text))
        })
    
    # Save processed output
    output_path = json_path.parent / f"{json_path.stem}_processed.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved processed data to: {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", help="Path to Docling JSON output")
    args = parser.parse_args()
    
    postprocess_json(args.input_json)
