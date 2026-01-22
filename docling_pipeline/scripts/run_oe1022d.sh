#!/bin/bash
set -e

# OE1022D Lock-in Amplifier PDF Conversion Script
# Converts pages 62-82 (ASCII command reference) as prototype

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
INPUT_PDF="$PROJECT_DIR/oe1022d-lockin.pdf"
OUTPUT_DIR="$PROJECT_DIR/knowledge_base/oe1022d"
PAGES="${1:-62-82}"  # Default to prototype pages, can be overridden

echo "╔═══════════════════════════════════════════════╗"
echo "║  OE1022D Lock-in Amplifier PDF Conversion     ║"
echo "╠═══════════════════════════════════════════════╣"
echo "║  Input:  $INPUT_PDF"
echo "║  Output: $OUTPUT_DIR"
echo "║  Pages:  $PAGES"
echo "╚═══════════════════════════════════════════════╝"
echo ""

# Check input file exists
if [ ! -f "$INPUT_PDF" ]; then
    echo "❌ Error: Input file not found: $INPUT_PDF"
    exit 1
fi

# Activate conda environment
echo "🔧 Activating conda environment..."
eval "$(conda shell.bash hook)"
conda activate doclingprj1

# Run conversion
echo "🚀 Starting conversion..."
echo ""
echo "💡 TIP: Monitor status in another terminal with:"
echo "   watch -n5 'cat $OUTPUT_DIR/run_*/status.json 2>/dev/null | jq . || echo Waiting...'"
echo ""

cd "$PROJECT_DIR"
python docling_pipeline/scripts/convert_pdf.py \
    --input "$INPUT_PDF" \
    --output "$OUTPUT_DIR" \
    --pages "$PAGES"

# Check result
LATEST_RUN=$(ls -td "$OUTPUT_DIR"/run_* 2>/dev/null | head -1)
if [ -n "$LATEST_RUN" ] && [ -f "$LATEST_RUN/status.json" ]; then
    echo ""
    echo "📊 Final Status:"
    cat "$LATEST_RUN/status.json" | python -m json.tool
fi

echo ""
echo "✅ Done!"
