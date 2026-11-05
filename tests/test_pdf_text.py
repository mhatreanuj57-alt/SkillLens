import fitz
import pytest

from src.pdf_text import MAX_UPLOAD_BYTES, PDFTextError, extract_pdf_text


def make_pdf(text: str = "Python and SQL experience.") -> bytes:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), text)
    data = document.tobytes()
    document.close()
    return data


def test_extracts_text_from_valid_pdf():
    assert "Python" in extract_pdf_text(make_pdf())


def test_rejects_non_pdf_signature():
    with pytest.raises(PDFTextError, match="signature"):
        extract_pdf_text(b"not a PDF")


def test_rejects_oversized_upload():
    with pytest.raises(PDFTextError, match="5 MB"):
        extract_pdf_text(b"%PDF-" + b"x" * MAX_UPLOAD_BYTES)


def test_rejects_scanned_pdf_without_text():
    document = fitz.open()
    document.new_page()
    data = document.tobytes()
    document.close()

    with pytest.raises(PDFTextError, match="No selectable text"):
        extract_pdf_text(data)