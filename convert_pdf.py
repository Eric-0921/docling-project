
import os
import argparse
import time
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Convert PDF using Docling with GPU acceleration")
    parser.add_argument("--input", type=str, required=True, help="Path to input PDF file")
    parser.add_argument("--output", type=str, default="output", help="Output directory")
    parser.add_argument("--max-pages", type=int, default=None, help="Max pages to convert")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Initializing Docling for file: {input_path}")

    # =========================================================================
    # Docling Configuration - A4000 Optimization (16GB VRAM)
    # =========================================================================
    from docling.document_converter import DocumentConverter
    from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
    from docling.datamodel.pipeline_options import (
        PdfPipelineOptions,
        ThreadedPdfPipelineOptions,
        TableFormerMode,
        RapidOcrOptions,
        EasyOcrOptions
    )
    from docling.datamodel.base_models import InputFormat
    from docling.document_converter import PdfFormatOption
    from docling.datamodel.settings import settings

    # 1. Global Settings: Enable Layout Batch Inference
    # CRITICAL: Must be set to enable batching in layout model
    # Range 16-32 is good for 16GB VRAM
    # CRITICAL: Must be set to enable batching in layout model
    # Range 16-32 is good for 16GB VRAM
    settings.perf.page_batch_size = 16
    
    # Enable CodeFormula model (new on Hugging Face) for better formula/code detection
    # This is handled automatically by Docling's updated pipeline if enabled in settings or options
    # Note: As of Docling v2.5+, layout models often include formula detection. 
    # To be explicit about using the advanced formula model potentially found on HF:
    pipeline_options = ThreadedPdfPipelineOptions(
        do_table_structure=True,
        do_code_enrichment=True, # Enable code/formula enrichment
        do_formula_enrichment=True,
    # ... rest of options


    # 2. GPU Accelerator Options
    accelerator_options = AcceleratorOptions(
        device=AcceleratorDevice.CUDA,
    )

    # 3. Pipeline Options
    # Use ThreadedPdfPipelineOptions for parallel processing of pages
    pipeline_options = ThreadedPdfPipelineOptions(
        do_table_structure=True,
        # Batch sizes tuned for A4000 (16GB) - Conservative values
        ocr_batch_size=32,       # Can go up to 48 if memory allows
        layout_batch_size=16,    # Matches page_batch_size
        table_batch_size=2,      # TableFormer is memory intensive
        do_code_enrichment=True, # Explicitly enable for CodeFormula
        do_formula_enrichment=True # Explicitly enable for CodeFormula
    )

    # 4. Model Selection: TableFormer ACCURATE
    # Best for complex tables in technical manuals
    pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
    pipeline_options.table_structure_options.do_cell_matching = True
    logger.info("Using TableFormer ACCURATE mode")

    # 5. Model Selection: RapidOCR (Torch Backend)
    # Recommended for GPU acceleration
    pipeline_options.ocr_options = RapidOcrOptions(backend="torch")
    logger.info("Using RapidOCR with Torch backend")

    # Initialize Converter
    converter = DocumentConverter(
        accelerator_options=accelerator_options,
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    # =========================================================================
    # Conversion Process
    # =========================================================================
    start_time = time.time()
    
    logger.info("Starting conversion...")
    
    # Run conversion
    result = converter.convert(
        input_path, 
        max_num_pages=args.max_pages
    )
    
    duration = time.time() - start_time
    logger.info(f"Conversion completed in {duration:.2f} seconds")

    # =========================================================================
    # Output Generation
    # =========================================================================
    
    # 1. Export Markdown
    md_output_path = output_dir / f"{input_path.stem}.md"
    markdown_content = result.document.export_to_markdown()
    with open(md_output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    logger.info(f"Saved Markdown to: {md_output_path}")

    # 2. Export JSON (for post-processing)
    json_output_path = output_dir / f"{input_path.stem}.json"
    json_content = result.document.export_to_dict()
    import json
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(json_content, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved structured JSON to: {json_output_path}")

if __name__ == "__main__":
    main()
