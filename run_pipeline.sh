#!/bin/bash
set -e

# Activate Environment (if needed, adjust path as necessary)
# source ~/anaconda3/etc/profile.d/conda.sh
# conda activate doclingprj1

INPUT_PDF="input/SMB100A_OperatingManual_en_23.pdf"
OUTPUT_DIR="output"
JSON_OUTPUT="${OUTPUT_DIR}/SMB100A_OperatingManual_en_23.json"

echo "=== Starting Pipeline ==="

# 1. Convert PDF to JSON/Markdown (GPU Accelerated)
echo "[1/2] Converting PDF..."
python scripts/convert_pdf.py --input "$INPUT_PDF" --output "$OUTPUT_DIR"

# 2. Post-process (Structure Extraction & Cleanup)
echo "[2/2] Post-processing JSON..."
python scripts/postprocess_kb.py "$JSON_OUTPUT"

echo "=== Pipeline Completed ==="
