import pdfplumber
from pathlib import Path

def load_pdf(pdf_path: str):
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Input file must be a PDF")

    return pdfplumber.open(pdf_path)
