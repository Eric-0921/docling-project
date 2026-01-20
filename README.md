# Docling PDF Conversion Project for SMB100A

This project implements a high-performance, GPU-accelerated pipeline to convert complex technical manuals (PDF) into AI-friendly structured knowledge bases (Markdown/JSON). It leverages the latest **Docling** capabilities, including NVIDA GPU acceleration and advanced models from Hugging Face.

## 🚀 Features

- **GPU Acceleration**: Fully optimized for NVIDIA GPUs (tested on A4000) using `RapidOCR` with Torch backend.
- **Advanced Layout Analysis**: Uses `DocLayNet` for precise layout understanding.
- **Complex Table Extraction**: Utilizes `TableFormer` in **ACCURATE** mode to perfectly reconstruct SCPI command tables.
- **Formula & Code Recognition**: Integrates `CodeFormula` model capabilities for enhanced technical content detection.
- **SCPI Awareness**: Custom post-processing to identify and preserve SCPI commands (`:SOURce:FREQuency:CW`) for downstream AI agents.

## 🛠️ Environment Setup

### Prerequisites
- **OS**: Linux (Ubuntu 22.04 recommended)
- **GPU**: NVIDIA GPU with CUDA 13.0+ support (16GB+ VRAM recommended for high batch sizes)
- **Manager**: Conda / Mamba

### Installation

1. **Create Conda Environment**
   ```bash
   conda create -n doclingprj1 python=3.10
   conda activate doclingprj1
   ```

2. **Install PyTorch (CUDA 13.0)**
   *Critical: Must match system CUDA version.*
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
   ```

3. **Install Docling & Extras**
   ```bash
   pip install "docling[easyocr,rapidocr,vlm]"
   ```

4. **Download Models**
   ```bash
   docling-tools models download
   ```

## 🧩 Models Used

This project uses a suite of SOTA models hosted on the [Docling Hugging Face](https://huggingface.co/docling-project) repository.

| Capability | Model / Engine | Configuration |
|------------|---------------|---------------|
| **Layout** | `DocLayNet` | `page_batch_size=16` (Grid Inference) |
| **Tables** | `TableFormer` | `TableFormerMode.ACCURATE` |
| **OCR** | `RapidOCR` | `backend="torch"` (GPU Accelerated) |
| **Formulas** | `CodeFormula` | `do_code_enrichment=True` |

## 🔗 References

- **Official GitHub**: [DS4SD/docling](https://github.com/DS4SD/docling)
- **Hugging Face Org**: [docling-project](https://huggingface.co/docling-project)
- **Documentation**: [Docling Docs](https://ds4sd.github.io/docling/)

## 📂 Project Structure

- `input/`: Raw PDF files (e.g., SMB100A manual).
- `output/`: Conversion results (Markdown, JSON).
- `scripts/`: Python scripts (`convert_pdf.py`, `postprocess_kb.py`).
- `docs/`: Project documentation.
- `.agent/skills/smb100a/`: Antigravity Skill definition.

## ⚡ Usage

### Convert PDF
Run the conversion script from the project root:

```bash
python scripts/convert_pdf.py --input input/SMB100A_OperatingManual_en_23.pdf --output output/
```

### Post-process (Structure & Clean)
```bash
python scripts/postprocess_kb.py output/SMB100A_OperatingManual_en_23.json
```
