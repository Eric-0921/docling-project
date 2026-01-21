#!/bin/bash
set -e

# Configuration
INPUT_PDF="input/SMB100A_OperatingManual_en_23.pdf"
OUTPUT_DIR="output"
ENV_NAME="doclingprj1"

# Activate Environment
echo "Activating Conda environment: $ENV_NAME"
source /home/tseng/anaconda3/etc/profile.d/conda.sh
conda activate $ENV_NAME

# Step 1: Docling Conversion
echo "Step 1: Running Docling Conversion..."
python scripts/convert_pdf.py --input "$INPUT_PDF" --output "$OUTPUT_DIR"

# Step 2: Identify Latest Run
LATEST_RUN=$(ls -td "$OUTPUT_DIR"/run_* | head -1)
echo "Latest Run Directory: $LATEST_RUN"

JSON_FILE="$LATEST_RUN/raw/$(basename "$INPUT_PDF" .pdf).json"
KB_OUTPUT="$OUTPUT_DIR/knowledge_base_final"

if [ ! -f "$JSON_FILE" ]; then
    echo "Error: JSON output not found at $JSON_FILE"
    exit 1
fi

# Step 3: Build Knowledge Base
echo "Step 2: Building Knowledge Base..."
python scripts/knowledge_builder_v2.py --input "$JSON_FILE" --output "$KB_OUTPUT"

echo "Pipeline Completed Successfully!"
echo "Knowledge Base located at: $KB_OUTPUT"
