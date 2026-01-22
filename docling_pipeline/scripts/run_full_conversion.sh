#!/bin/bash
set -e

# Configuration
INPUT_PDF="oe1022d-lockin.pdf"
RUN_TIMESTAMP=$(date +%Y%m%d_%H%M%S)
VERSION="v0.2.0"
BASE_OUTPUT_DIR="knowledge_base/archive/oe1022d_runs"
FULL_RUN_DIR="${BASE_OUTPUT_DIR}/full_run_${RUN_TIMESTAMP}"

echo "=== Starting Full OE1022D Conversion [${RUN_TIMESTAMP}] ==="
echo "Input: ${INPUT_PDF}"
echo "Output Dir: ${FULL_RUN_DIR}"

mkdir -p "$FULL_RUN_DIR"

# 1. Docling Conversion (PDF -> JSON/MD)
echo ">>> Running Docling Conversion..."
# Note: output arg in convert_pdf.py creates a subdirectory based on timestamp/run_id
# We want to capture that run_id to find the files later.
python docling_pipeline/scripts/convert_pdf.py \
    --input "$INPUT_PDF" \
    --output "$FULL_RUN_DIR"

# 2. Locate Generated JSON
# convert_pdf creates a folder like 'run_YYYYMMDD_HHMMSS' inside the output dir
GENERATED_RUN_DIR=$(find "$FULL_RUN_DIR" -maxdepth 1 -type d -name "run_*" | sort -r | head -n 1)

if [ -z "$GENERATED_RUN_DIR" ]; then
    echo "Error: Could not find generated run directory in $FULL_RUN_DIR"
    exit 1
fi

echo ">>> Found Generated Run Dir: $GENERATED_RUN_DIR"
JSON_FILE="${GENERATED_RUN_DIR}/raw/oe1022d-lockin.json"

if [ ! -f "$JSON_FILE" ]; then
    echo "Error: JSON file not found at $JSON_FILE"
    exit 1
fi

# 3. Generate Structured Markdown (Post-processing)
echo ">>> Generating Structured Markdown..."
FINAL_FILENAME="oe1022d-lockin_${VERSION}_${RUN_TIMESTAMP}.md"
FINAL_PATH="${GENERATED_RUN_DIR}/${FINAL_FILENAME}"

python docling_pipeline/scripts/generate_structured_md.py "$JSON_FILE" "$FINAL_PATH"

echo ">>> Conversion Complete!"
echo "Final Artifact: $FINAL_PATH"

# 4. (Optional) Copy to Production Staging or Print Location for Agent
echo "Artifact Location: $FINAL_PATH"
