import os
import re
import json
import yaml
import sys
from openai import OpenAI

# Configuration
INPUT_FILE = "docs/visual_optimized/SMB100A_OperatingManual_cn_sample.md"
OUTPUT_FILE = "docs/visual_optimized/SMB100A_OperatingManual_cn_ai_tables.md"
API_KEY_FILE = "api_keys.yml"

def load_api_key(path):
    try:
        with open(path, 'r') as f:
            for line in f:
                if 'deepseek_api_key' in line:
                    return line.split(':', 1)[1].strip()
    except Exception as e:
        print(f"Error loading API key: {e}")
    return os.environ.get("DEEPSEEK_API_KEY")

def get_client(api_key):
    return OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def process_table_block(client, lines_block):
    """
    Sends a block of text (lines) to DeepSeek to reformat as a valid Markdown table.
    """
    input_text = "".join(lines_block)
    
    system_prompt = """You are an expert technical document formatter.
Your task is to take a raw, messy text block that represents a table (extracted from PDF) and convert it into a clean, valid Markdown table.
Rules:
1. Preserve all technical content (numbers, parameter names, units) exactly.
2. Fix broken headers: Merge multi-line headers into single rows where appropriate.
3. Fix broken rows: If a row is split across lines, merge it.
4. Remove leader dots (e.g., "Parameter.......... 50") and keep only the value.
5. Remove any PDF artifact lines (like page numbers) if they are inside the table.
6. Return the result as a JSON object with a single key "markdown" containing the string of the formatted table.
7. If the input is NOT a table (just text with pipes), try to format it as a table if it makes sense, or return it as text using the same JSON structure.
"""
    
    user_prompt = f"Input text block:\n```\n{input_text}\n```\n\nPlease reformat this into a clean Markdown table."

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        content = response.choices[0].message.content
        data = json.loads(content)
        return data.get("markdown", input_text)
    except Exception as e:
        print(f"Error processing table block: {e}")
        return input_text

def main():
    api_key = load_api_key(API_KEY_FILE)
    if not api_key:
        print("Could not find DeepSeek API key.")
        return

    client = get_client(api_key)

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Input file not found: {INPUT_FILE}")
        return

    print(f"Processing {len(lines)} lines...")
    
    # Open output file for streaming
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        
        current_block = []
        in_table = False
        
        for i, line in enumerate(lines):
            # Progress marker
            if i % 1000 == 0:
                print(f"Processed {i}/{len(lines)} lines...")
                
            has_pipe = '|' in line
            
            if has_pipe:
                if not in_table:
                    in_table = True
                current_block.append(line)
            else:
                if in_table:
                    # End of table block -> Process
                    if len(current_block) >= 2: 
                        print(f"  Fixing table block at line {i - len(current_block)} ({len(current_block)} lines)")
                        fixed_table = process_table_block(client, current_block)
                        if not fixed_table.endswith('\n'):
                            fixed_table += '\n'
                        f_out.write(fixed_table)
                    else:
                        # Too short, just write as is
                        f_out.writelines(current_block)
                    
                    # Ensure we flush
                    f_out.flush()
                    
                    current_block = []
                    in_table = False
                    
                f_out.write(line)

        # Handle last block
        if current_block:
             if len(current_block) >= 2:
                 print(f"  Fixing final table block ({len(current_block)} lines)")
                 fixed_table = process_table_block(client, current_block)
                 if not fixed_table.endswith('\n'):
                     fixed_table += '\n'
                 f_out.write(fixed_table)
             else:
                 f_out.writelines(current_block)
    
    print(f"Done. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
