
import os
import argparse
import time
import json
import threading
import psutil
import sys
import traceback
from pathlib import Path
from datetime import datetime
import logging
import signal

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

# Setup Logging to File AND console for heartbeat
logging.basicConfig(level=logging.INFO, filename='docling_conversion.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Also add console handler for critical messages
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)


def parse_page_range(page_str: str) -> tuple:
    """Parse page range like '62-82' into (start, end) tuple for Docling.
    
    Docling uses page_range=(start, end) tuple, so we convert:
    - '62-82' -> (62, 82)
    - '62,65,70' -> uses min and max: (62, 70) with a warning
    - '62' -> (62, 62) for single page
    """
    pages = []
    for part in page_str.split(','):
        part = part.strip()
        if '-' in part:
            start, end = part.split('-', 1)
            pages.extend([int(start), int(end)])
        else:
            pages.append(int(part))
    
    if len(pages) == 0:
        return (1, sys.maxsize)
    
    min_page = min(pages)
    max_page = max(pages)
    
    if len(set(pages)) > 2:
        logger.warning(f"Docling only supports contiguous page ranges. Using ({min_page}, {max_page}) which includes all pages in between.")
    
    return (min_page, max_page)


class StatusFile:
    """Manages a status.json file for tracking conversion progress."""
    
    def __init__(self, output_dir: Path):
        self.path = output_dir / "status.json"
        self.start_time = datetime.now()
        self._data = {
            "status": "initializing",
            "start_time": self.start_time.isoformat(),
            "elapsed_seconds": 0,
            "last_heartbeat": self.start_time.isoformat(),
            "pages_requested": None,
            "error_message": None,
            "output_files": []
        }
        self._write()
    
    def _write(self):
        self._data["elapsed_seconds"] = (datetime.now() - self.start_time).total_seconds()
        self._data["last_heartbeat"] = datetime.now().isoformat()
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)
    
    def set_running(self, pages: list = None):
        self._data["status"] = "running"
        self._data["pages_requested"] = pages
        self._write()
    
    def heartbeat(self):
        """Update heartbeat timestamp."""
        self._write()
    
    def set_completed(self, output_files: list):
        self._data["status"] = "completed"
        self._data["output_files"] = output_files
        self._write()
    
    def set_failed(self, error_message: str):
        self._data["status"] = "failed"
        self._data["error_message"] = error_message
        self._write()

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
    parser.add_argument("--max-pages", type=int, default=None, help="Max pages to convert (from start)")
    parser.add_argument("--pages", type=str, default=None, help="Pages to convert (e.g. '62-82' or '1,2,3' or '1-5,10')")
    args = parser.parse_args()

    console = Console()
    input_path = Path(args.input)
    if not input_path.exists():
        console.print(f"[bold red]Error: Input file {input_path} not found![/bold red]")
        sys.exit(1)

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

    # Status tracking
    status_file = StatusFile(run_output_dir)
    
    # Parse pages if specified
    page_range = None
    if args.pages:
        page_range = parse_page_range(args.pages)
        console.print(f"[cyan]Will convert page range: {page_range[0]} to {page_range[1]}[/cyan]")
        logger.info(f"Parsed page range '{args.pages}' -> {page_range}")
    
    status_file.set_running(pages=list(range(page_range[0], page_range[1]+1)) if page_range else None)
    
    # UI Setup
    gpu_monitor = GpuMonitor()
    gpu_monitor.start()

    # Docling Configuration
    settings.perf.page_batch_size = 16
    # settings.perf.do_code_formula = True # Removed: Not supported in this version of Docling settings

    accelerator_options = AcceleratorOptions(device=AcceleratorDevice.CUDA)
    pipeline_options = ThreadedPdfPipelineOptions(
        do_ocr=True,
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
            conversion_result = {"doc": None, "error": None}
            last_heartbeat = [time.time()]  # Use list to allow modification in closure

            def run_conversion():
                try:
                    if page_range:
                        logger.info(f"Converting page range: {page_range}")
                        res = converter.convert(input_path, page_range=page_range)
                    else:
                        max_pages = args.max_pages if args.max_pages else sys.maxsize
                        res = converter.convert(input_path, max_num_pages=max_pages)
                    conversion_result['doc'] = res
                except Exception as e:
                    conversion_result['error'] = traceback.format_exc()
                    logger.error(f"Conversion failed: {e}", exc_info=True)
                finally:
                    conversion_done.set()

            conv_thread = threading.Thread(target=run_conversion)
            conv_thread.start()

            while not conversion_done.is_set():
                # Update Dashboard
                cpu_util = psutil.cpu_percent()
                mem_util = psutil.virtual_memory().percent
                elapsed = time.time() - start_time
                
                # Heartbeat every 30 seconds (for SSH sessions and logs)
                if time.time() - last_heartbeat[0] >= 30:
                    logger.warning(f"[HEARTBEAT] Conversion running for {elapsed:.0f}s, GPU: {gpu_monitor.gpu_util}%, VRAM: {gpu_monitor.mem_used:.1f}GB")
                    status_file.heartbeat()
                    last_heartbeat[0] = time.time()
                
                # Create Stats Table
                table = Table(box=box.SIMPLE)
                table.add_column("Resource", style="dim")
                table.add_column("Value", style="bold")
                table.add_row("GPU Util", f"{gpu_monitor.gpu_util}%")
                table.add_row("VRAM", f"{gpu_monitor.mem_used:.1f}GB / {gpu_monitor.mem_total:.1f}GB")
                table.add_row("CPU Util", f"{cpu_util}%")
                table.add_row("RAM Util", f"{mem_util}%")
                table.add_row("Elapsed", f"{elapsed:.1f}s")
                table.add_row("Status File", str(status_file.path))
                
                layout = create_layout(input_path.name, run_id)
                layout["main"].update(Panel(table, title="System Resources", border_style="green"))
                layout["footer"].update(Panel(f"🔄 Converting... Check status: cat {status_file.path}", style="yellow"))
                
                live.update(layout)
                time.sleep(0.5)

            # Conversion Done - check for errors
            conv_thread.join()
            
            if conversion_result['error']:
                error_msg = conversion_result['error']
                console.print(f"[bold red]❌ Conversion FAILED![/bold red]")
                console.print(f"[red]{error_msg}[/red]")
                status_file.set_failed(error_msg)
                sys.exit(1)
            
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

            # Mark as completed
            output_files = [str(md_path), str(json_path)]
            status_file.set_completed(output_files)
            
            console.print(f"[bold green]✅ Conversion COMPLETED![/bold green]")
            console.print(f"[green]Output saved to: {run_output_dir}[/green]")
            console.print(f"[dim]Elapsed time: {time.time() - start_time:.2f}s[/dim]")

        except Exception as e:
            error_msg = traceback.format_exc()
            console.print(f"[bold red]❌ Error during conversion: {e}[/bold red]")
            console.print(f"[red]{error_msg}[/red]")
            status_file.set_failed(error_msg)
            logger.error(f"Conversion failed: {e}", exc_info=True)
            sys.exit(1)
        finally:
            gpu_monitor.stop()

if __name__ == "__main__":
    main()
