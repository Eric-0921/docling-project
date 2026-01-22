#!/bin/bash
set -e

# Default paths suitable for project root execution
INPUT_PDF="instrument_control/manuals/SMB100A_OperatingManual_en_23.pdf"
# Fallback to local input if exists
if [ ! -f "$INPUT_PDF" ]; then
    INPUT_PDF="docling_pipeline/input/SMB100A_OperatingManual_en_23.pdf"
fi

OUTPUT_DIR="docling_pipeline/output"
CONFIG="docling_pipeline/config/smb100a.yaml"

echo "=== Starting SMB100A Pipeline ==="
echo "Input: $INPUT_PDF"

# 1. Convert
echo "[1/2] Converting PDF..."
python docling_pipeline/scripts/convert_pdf.py --input "$INPUT_PDF" --output "$OUTPUT_DIR"

# Find Latest Run
LATEST_RUN=$(ls -td "$OUTPUT_DIR"/run_* | head -1)
echo "Latest Run: $LATEST_RUN"

# Filename extraction (basename without extension)
FILENAME=$(basename -- "$INPUT_PDF")
FILENAME="${FILENAME%.*}"
JSON_OUTPUT="${LATEST_RUN}/raw/${FILENAME}.json"

# 2. Build KB
echo "[2/2] Building Knowledge Base..."
if [ -f "$JSON_OUTPUT" ]; then
    python docling_pipeline/scripts/knowledge_builder_v3.py \
        --input "$JSON_OUTPUT" \
        --output "${LATEST_RUN}/knowledge_base" \
        --config "$CONFIG"
    echo "Knowledge Base generated at ${LATEST_RUN}/knowledge_base"
else
    echo "Error: JSON output not found at $JSON_OUTPUT"
    exit 1
fi
