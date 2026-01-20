
import os
import argparse
import time
import json
import threading
import psutil
import sys
from pathlib import Path
from datetime import datetime
import logging

# Rich Imports
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich import box

# GPU Monitoring
import pynvml

# Docling Imports
from docling.document_converter import DocumentConverter
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    ThreadedPdfPipelineOptions,
    TableFormerMode,
    RapidOcrOptions
)
from docling.datamodel.base_models import InputFormat
from docling.document_converter import PdfFormatOption
from docling.datamodel.settings import settings

# Setup Logging to File only (to not mess up Rich display)
logging.basicConfig(level=logging.INFO, filename='docling_conversion.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GpuMonitor:
    def __init__(self):
        self.gpu_util = 0
        self.mem_used = 0
        self.mem_total = 0
        self.running = False
        try:
            pynvml.nvmlInit()
            self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            self.available = True
        except:
            self.available = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._update_loop, daemon=True)
        self.thread.start()

    def _update_loop(self):
        while self.running:
            if self.available:
                try:
                    util = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
                    mem = pynvml.nvmlDeviceGetMemoryInfo(self.handle)
                    self.gpu_util = util.gpu
                    self.mem_used = mem.used / 1024**3
                    self.mem_total = mem.total / 1024**3
                except:
                    pass
            time.sleep(1)

    def stop(self):
        self.running = False
        if self.available:
            try:
                pynvml.nvmlShutdown()
            except:
                pass

def create_layout(input_name, run_id):
    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["header"].update(Panel(f"Docling Conversion Pipeline | File: {input_name} | RunID: {run_id}", style="bold cyan"))
    return layout

def main():
    parser = argparse.ArgumentParser(description="Convert PDF using Docling with GPU acceleration and Rich Dashboard")
    parser.add_argument("--input", type=str, required=True, help="Path to input PDF file")
    parser.add_argument("--output", type=str, default="output", help="Output directory root")
    parser.add_argument("--max-pages", type=int, default=None, help="Max pages to convert")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        console = Console()
        console.print(f"[bold red]Error: Input file {input_path} not found![/bold red]")
        return

    # Setup Run ID and Directories
    run_id = datetime.now().strftime("run_%Y%m%d_%H%M%S")
    run_output_dir = Path(args.output) / run_id
    raw_output_dir = run_output_dir / "raw"
    raw_output_dir.mkdir(parents=True, exist_ok=True)

    # Save Config
    config = vars(args)
    config["settings"] = {
        "page_batch_size": 16,
        "ocr_batch_size": 32,
        "table_mode": "TableFormer.ACCURATE",
        "ocr_engine": "RapidOCR(torch)",
        "code_formula": True
    }
    with open(run_output_dir / "config.json", "w") as f:
        json.dump(config, f, indent=2)

    # UI Setup
    console = Console()
    gpu_monitor = GpuMonitor()
    gpu_monitor.start()

    # Docling Configuration
    settings.perf.page_batch_size = 16
    # settings.perf.do_code_formula = True # Removed: Not supported in this version of Docling settings

    accelerator_options = AcceleratorOptions(device=AcceleratorDevice.CUDA)
    pipeline_options = ThreadedPdfPipelineOptions(
        do_table_structure=True,
        ocr_batch_size=32,
        layout_batch_size=16,
        table_batch_size=2,
        do_code_enrichment=True,
        do_formula_enrichment=True
    )
    pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
    pipeline_options.table_structure_options.do_cell_matching = True
    pipeline_options.ocr_options = RapidOcrOptions(backend="torch")

    pipeline_options.accelerator_options = accelerator_options

    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
    )

    # Conversion Loop with Dashboard
    start_time = time.time()
    
    with Live(create_layout(input_path.name, run_id), refresh_per_second=4, console=console) as live:
        try:
            # Note: Docling's convert() is blocking. Ideally, we would iterate if Docling supported generator.
            # Since it doesn't easily expose granular progress for a single file, 
            # we will show a "Processing..." spinner and update system stats.
            
            # Since we can't easily hook into Docling's internal loop without patching,
            # we run conversion in a thread and update the UI specific to resources.
            
            conversion_done = threading.Event()
            conversion_result = {}

            def run_conversion():
                max_pages = args.max_pages if args.max_pages else sys.maxsize
                res = converter.convert(input_path, max_num_pages=max_pages)
                conversion_result['doc'] = res
                conversion_done.set()

            conv_thread = threading.Thread(target=run_conversion)
            conv_thread.start()

            while not conversion_done.is_set():
                # Update Dashboard
                cpu_util = psutil.cpu_percent()
                mem_util = psutil.virtual_memory().percent
                
                # Create Stats Table
                table = Table(box=box.SIMPLE)
                table.add_column("Resource", style="dim")
                table.add_column("Value", style="bold")
                table.add_row("GPU Util", f"{gpu_monitor.gpu_util}%")
                table.add_row("VRAM", f"{gpu_monitor.mem_used:.1f}GB / {gpu_monitor.mem_total:.1f}GB")
                table.add_row("CPU Util", f"{cpu_util}%")
                table.add_row("RAM Util", f"{mem_util}%")
                table.add_row("Elapsed", f"{time.time() - start_time:.1f}s")
                
                layout = create_layout(input_path.name, run_id)
                layout["main"].update(Panel(table, title="System Resources", border_style="green"))
                layout["footer"].update(Panel(f"Converting... Please wait. Check logs for details.", style="yellow"))
                
                live.update(layout)
                time.sleep(0.5)

            # Conversion Done
            conv_thread.join()
            result = conversion_result['doc']
            
            # Final Update
            layout = create_layout(input_path.name, run_id)
            layout["main"].update(Panel(f"[bold green]Conversion Completed![/bold green]\nTime: {time.time() - start_time:.2f}s", title="Status"))
            live.update(layout)

            # Export
            console.print("[bold]Exporting results...[/bold]")
            
            # Markdown
            md_path = run_output_dir / f"{input_path.stem}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(result.document.export_to_markdown())
            
            # JSON (Raw)
            json_path = raw_output_dir / f"{input_path.stem}.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(result.document.export_to_dict(), f, ensure_ascii=False, indent=2)

            console.print(f"[green]Done! Output saved to: {run_output_dir}[/green]")

        except Exception as e:
            console.print(f"[bold red]Error during conversion: {e}[/bold red]")
            logger.error(f"Conversion failed: {e}", exc_info=True)
        finally:
            gpu_monitor.stop()

if __name__ == "__main__":
    main()
