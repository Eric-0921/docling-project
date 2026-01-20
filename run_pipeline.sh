#!/bin/bash
set -e

# Activate Environment (if needed, adjust path as necessary)
# source ~/anaconda3/etc/profile.d/conda.sh
# conda activate doclingprj1

INPUT_PDF="input/SMB100A_OperatingManual_en_23.pdf"
OUTPUT_DIR="output"
JSON_OUTPUT="${OUTPUT_DIR}/SMB100A_OperatingManual_en_23.json"

echo "=== Starting Pipeline ==="

# 1. Convert PDF to JSON/Markdown (GPU Accelerated w/ Dashboard)
echo "[1/2] Converting PDF..."
# Output will be generated in output/run_YYYYMMDD_HHMMSS/
python scripts/convert_pdf.py --input "$INPUT_PDF" --output "$OUTPUT_DIR"

# Find the latest Run ID directory
LATEST_RUN=$(ls -td "$OUTPUT_DIR"/run_* | head -1)
echo "Latest Run: $LATEST_RUN"

JSON_OUTPUT="${LATEST_RUN}/raw/SMB100A_OperatingManual_en_23.json"

# 2. Post-process (Structure Extraction & Cleanup)
if [ -f "$JSON_OUTPUT" ]; then
    echo "[2/2] Post-processing JSON..."
    python scripts/postprocess_kb.py "$JSON_OUTPUT"
    echo "Knowledge Base generated in: ${LATEST_RUN}/knowledge_base/"
else
    echo "Error: Raw JSON not found at $JSON_OUTPUT"
    exit 1
fi

echo "=== Pipeline Completed ==="
