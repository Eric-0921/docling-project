---
name: Docling PDF Converter
description: Use Docling to convert PDF documents into structured Markdown/JSON knowledge bases. Optimized for NVIDIA GPUs.
---

# Docling PDF Converter Skill

This skill allows you to convert complex PDF documents (especially technical manuals with tables) into AI-friendly formats using Docling.

## Capabilities

- **Layout Analysis**: Uses DocLayNet to identify headers, paragraphs, and figures.
- **Table Structure**: Uses TableFormer (ACCURATE mode) to reconstruct complex SCPI command tables.
- **OCR**: Uses RapidOCR (Torch backend) for GPU-accelerated text recognition.
- **Export**: Generates Markdown and structured JSON.

## Usage

Run the conversion script located at `convert_pdf.py`.

```bash
python convert_pdf.py
```

## Configuration

The script is pre-configured for NVIDIA A4000 GPUs:
- `page_batch_size = 16`
- `ocr_batch_size = 32`
- `table_batch_size = 2`

## Output

Outputs are saved in the `output/` directory by default.
- `filename.md`: Markdown version for RAG.
- `filename.json`: Structured data for post-processing.
