#!/bin/bash
set -e

# Configuration
INPUT_PDF="oe1022d-lockin.pdf"
CONFIG_FILE="docling_pipeline/config/oe1022d.yaml"
OUTPUT_DIR="knowledge_base/oe1022d"

echo "Starting OE1022D Pipeline..."

# 1. Convert PDF (If needed, or use existing JSON if comfortable)
# For now, we assume we might want to skip conversion if JSON exists to save time during dev
# echo "Converting PDF..."
# python docling_pipeline/scripts/convert_pdf.py --input "$INPUT_PDF" --output "$OUTPUT_DIR"

# 2. Build Knowledge Base
echo "Building Knowledge Base..."
# Find the latest run in the output directory if not specified
# This logic might need improvement to pick the RIGHT json. 
# For now, let's assume the user passes the JSON path or we pick the latest.
# But convert_pdf outputs to 'output/<run_id>/raw/'. 
# This script is a bit of a wrapper.

# Simpler approach: User runs convert_pdf first, then this script points to the JSON?
# Or this script runs everything.

# Let's run builder on a specific JSON for now, or let arg parsing handle it.
# Actually, let's make this script accept the JSON input.

if [ -z "$1" ]; then
    echo "Usage: ./run_oe1022d.sh <path_to_docling_json>"
    echo "Example: ./run_oe1022d.sh prototype_output/run_2024.../raw/oe1022d-lockin.json"
    exit 1
fi

JSON_PATH=$1

python docling_pipeline/scripts/knowledge_builder_v3.py \
    --input "$JSON_PATH" \
    --output "$OUTPUT_DIR" \
    --config "$CONFIG_FILE"

echo "Done. Knowledge Base in $OUTPUT_DIR"
