
import json
import argparse
import difflib
import sys
from pathlib import Path
from typing import List, Dict

# Path to the Knowledge Base (Relative to this script)
# Structure:
# skills/scpi_expert/tools/query_kb.py
# skills/scpi_expert/knowledge_base/index.json
CURRENT_DIR = Path(__file__).parent.resolve()
KB_INDEX_PATH = CURRENT_DIR.parent / "knowledge_base" / "index.json"
KB_ROOT_PATH = CURRENT_DIR.parent / "knowledge_base"

def load_index() -> Dict:
    if not KB_INDEX_PATH.exists():
        print(f"Error: Knowledge Base index not found at {KB_INDEX_PATH}", file=sys.stderr)
        sys.exit(1)
    
    with open(KB_INDEX_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def search_index(query: str, index: Dict, top_k: int = 5) -> List[Dict]:
    scpi_index = index.get("scpi_index", {})
    structure = index.get("structure", [])
    
    # 1. Direct Key Match (for SCPI commands)
    # user query: "Set frequency" -> match specific commands?
    # user query: ":FREQ" -> match keys
    
    results = []
    
    # Prepare search corpus
    # List of (score_key, item_data)
    corpus = []
    
    # Add SCPI Commands
    for cmd, data in scpi_index.items():
        corpus.append((cmd, data))
        
    # Add Sections (using title)
    for section in structure:
        if section['type'] == 'section':
             corpus.append((section['title'], section))
    
    # Scoring
    # We use difflib.SequenceMatcher for similarity
    scored = []
    query_lower = query.lower()
    
    for key, data in corpus:
        # Score 1: Key similarity
        s1 = difflib.SequenceMatcher(None, query_lower, key.lower()).ratio()
        
        # Score 2: Title inclusion (if query is "frequency", match ":SOURce:FREQuency")
        s2 = 0.0
        if query_lower in key.lower():
            s2 = 0.8
        
        # Combined Score
        final_score = max(s1, s2)
        
        if final_score > 0.3: # Threshold
            scored.append((final_score, data))
            
    # Sort
    scored.sort(key=lambda x: x[0], reverse=True)
    
    return [item for score, item in scored[:top_k]]

def main():
    parser = argparse.ArgumentParser(description="Query the SMB100A Knowledge Base")
    parser.add_argument("query", type=str, help="Search query (e.g., 'frequency', ':POWer')")
    parser.add_argument("--top", type=int, default=5, help="Number of results to return")
    args = parser.parse_args()
    
    data = load_index()
    results = search_index(args.query, data, args.top)
    
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
