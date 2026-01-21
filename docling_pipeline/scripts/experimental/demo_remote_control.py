
import json
import logging
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
from rich.console import Console
from rich.panel import Panel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_demo_pdf(input_path: Path, output_path: Path, start_page: int, num_pages: int = 20):
    logger.info(f"Extracting {num_pages} pages starting from {start_page}...")
    reader = PdfReader(str(input_path))
    writer = PdfWriter()
    
    count = 0
    total_available = len(reader.pages)
    
    for i in range(start_page, min(start_page + num_pages, total_available)):
        writer.add_page(reader.pages[i])
        count += 1
        
    with open(output_path, "wb") as f:
        writer.write(f)
    logger.info(f"Created demo PDF with {count} pages: {output_path}")

def run_docling_conversion(input_path: Path, output_dir: Path):
    logger.info("Initializing Docling converter...")
    
    # Configure Pipeline Options
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
    pipeline_options.generate_page_images = True # Useful for debugging visuals if needed
    
    doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    logger.info(f"Converting {input_path}...")
    conv_result = doc_converter.convert(input_path)
    
    # Export JSON
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{input_path.stem}.json"
    
    # Get JSON dict
    doc_dict = conv_result.document.export_to_dict()
    
    # Inject implicit confidence if available (Docling v2.34+ might put it in conversion_result, not doc export)
    # We want to inspect "conv_result" object itself to see if we can find confidence scores 
    # and manually inject them into our JSON if export_to_dict doesn't include them.
    
    # Check if confidence is in the doc dict already
    logger.info(f"Keys in Doc Dict: {list(doc_dict.keys())}")
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(doc_dict, f, indent=2)
    
    logger.info(f"Saved JSON to {json_path}")
    return doc_dict, json_path

def analyze_scpi_structures(doc_dict):
    """
    Simple analysis to see if we can find Table/List structures that look like SCPI commands.
    """
    console = Console()
    console.print(Panel("Analyzing SCPI Structures"))
    
    tables = doc_dict.get("tables", [])
    console.print(f"Found {len(tables)} tables.")
    
    scpi_candidates = []
    
    # Analyze text items for SCPI patterns (starting with :)
    texts = doc_dict.get("texts", [])
    for item in texts:
        text = item.get("text", "").strip()
        if text.startswith(":") and len(text) > 5 and text.isupper():
             scpi_candidates.append(text)
             
    console.print(f"Potential SCPI Command Headers found (Text): {len(scpi_candidates)}")
    if scpi_candidates:
        console.print(f"Sample: {scpi_candidates[:5]}")

    # Analyze groups if available for structure
    if 'groups' in doc_dict:
        console.print(f"Groups (Hierarchy) found: {len(doc_dict['groups'])}")
    else:
        console.print("[yellow]No 'groups' found in JSON export (Hierarchy missing?)[/yellow]")

if __name__ == "__main__":
    console = Console()
    console.print(Panel.fit("[bold green]Docling SCPI Demo[/bold green]"))
    
    base_dir = Path("/home/tseng/git/docling-project")
    input_pdf = base_dir / "input/SMB100A_OperatingManual_en_23.pdf"
    
    # Demo Setup
    demo_pdf_path = base_dir / "input/demo_remote_control.pdf"
    demo_output_dir = base_dir / "output/demo_scpi"
    
    # 1. Prepare PDF
    if not demo_pdf_path.exists():
        setup_demo_pdf(input_pdf, demo_pdf_path, 282, 20)
    else:
        console.print("[yellow]Demo PDF already exists, using existing.[/yellow]")
        
    # 2. Run Conversion
    doc_dict, json_path = run_docling_conversion(demo_pdf_path, demo_output_dir)
    
    # 3. Analyze
    analyze_scpi_structures(doc_dict)
