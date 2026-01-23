import sys
import os
import time
import json

# Add project root to path so we can import translation_pipeline
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ai_adapter.translation_agent.core.deepseek_client import DeepSeekClient
from ai_adapter.translation_agent.core.scpi_guard import SCPIGuard
from ai_adapter.translation_agent.core.monitor import TaskMonitor
from ai_adapter.translation_agent.processor.markdown_parser import MarkdownParser
from rich.live import Live

def main():
    print("Initializing DeepSeek Advanced Translation Pipeline...")
    
    input_file = "docs/SMB100A_OperatingManual_en_23.md"
    
    # Define output path based on rules: database/production/i18n/zh-cn/v{version}/
    version = "v1.0_20260123"
    output_dir = f"database/production/i18n/zh-cn/{version}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"SMB100A_OperatingManual_cn_{version}.md")
    
    # Initialize Components
    client = DeepSeekClient()
    guard = SCPIGuard()
    parser = MarkdownParser(max_chars=2000) # Slightly larger chunks due to caching efficienty
    
    # Read Content
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_content = f.read()
        
    # Phase 1: Chunking (Raw)
    print("Chunking document...")
    chunks = parser.parse_and_chunk(raw_content)
    print(f"Generated {len(chunks)} chunks.")
    
    # Validating Chunks
    print(f"Total chunks to process: {len(chunks)}")

    # Checkpoint Logic
    checkpoint_file = "translation_checkpoint.json"
    start_index = 0
    translated_chunks = []
    
    if os.path.exists(checkpoint_file):
        print("Found checkpoint. Resuming...")
        try:
            with open(checkpoint_file, 'r') as f:
                ckpt = json.load(f)
                start_index = ckpt.get("index", 0)
                translated_chunks = ckpt.get("chunks", [])
                monitor_data = ckpt.get("monitor", {})
                print(f"Resuming from chunk {start_index}...")
                
                # Restore monitor state if possible (simplified)
                # Ideally TaskMonitor should verify serialized state
        except Exception as e:
            print(f"Failed to load checkpoint: {e}")

    # Initialize Monitor (Adjust for resume)
    monitor = TaskMonitor(total_chunks=len(chunks))
    monitor.processed_chunks = start_index 
    # Note: Cost might be reset if not saved, but that's acceptable for now.
    
    try:
        with Live(monitor.display(), refresh_per_second=4) as live:
            for i in range(start_index, len(chunks)):
                chunk = chunks[i]
                
                try:
                    # Step 1: Protect SCPI/Code
                    protected_text = guard.protect(chunk)
                    
                    # Step 2: Translate via DeepSeek (JSON Mode)
                    translated_protected_text, usage = client.translate(protected_text)
                    
                    # Update Monitor
                    monitor.update_metrics(usage)
                    live.update(monitor.display())
                    
                    # Step 3: Restore SCPI/Code
                    final_text = guard.restore(translated_protected_text)
                    
                    translated_chunks.append(final_text)

                    # Save Checkpoint every 5 chunks
                    if (i + 1) % 5 == 0:
                        with open(checkpoint_file, 'w') as f:
                            json.dump({
                                "index": i + 1,
                                "chunks": translated_chunks,
                                "monitor": {
                                    "cost": monitor.total_cost
                                }
                            }, f)

                except Exception as inner_e:
                    live.console.print(f"[red]Error processing chunk {i}: {inner_e}[/red]")
                    # Try one retry or just append placeholder? 
                    # For now, let's append original and continue to avoid full crash
                    translated_chunks.append(chunk) 
                    with open("translation_errors.log", "a") as err_f:
                        err_f.write(f"Chunk {i} failed: {inner_e}\n")
                        
    except Exception as e:
        print(f"Fatal Error: {e}")
        import traceback
        traceback.print_exc()
        with open("fatal_error.log", "w") as f:
            f.write(str(e))
            f.write(traceback.format_exc())
            
    print("Translation finished (or stopped).")
    print(f"Total Cost: ${monitor.total_cost:.4f}")
    print(f"Saving to {output_file}...")
    
    # Metadata Header
    header = f"""---
title: SMB100A 射频与微波信号发生器操作手册 (中文版)
version: 1.0.0
generated_date: {time.strftime('%Y-%m-%d')}
source_document: {input_file}
translator_engine: DeepSeek-V3
pipeline_version: 1.2.0
status: Final
cost: ${monitor.total_cost:.4f}
---

"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(header + '\n\n'.join(translated_chunks))
    
    # Cleanup checkpoint if successful
    if len(translated_chunks) == len(chunks):
        if os.path.exists(checkpoint_file):
            os.remove(checkpoint_file)
        
    print("Success! Check the output file for placeholder verification.")

if __name__ == "__main__":
    main()
