import fitz

MAX_UPLOAD_BYTES = 5 * 1024 * 1024
MAX_PAGES = 100


class PDFTextError(ValueError):
    """A PDF cannot be safely or usefully read by this MVP."""


def extract_pdf_text(data: bytes) -> str:
    if not data:
        raise PDFTextError("The uploaded file is empty.")
    if len(data) > MAX_UPLOAD_BYTES:
        raise PDFTextError("The PDF is larger than the 5 MB upload limit.")
    if b"%PDF-" not in data[:1024]:
        raise PDFTextError("The uploaded file does not have a valid PDF signature.")

    try:
        document = fitz.open(stream=data, filetype="pdf")
    except (fitz.FileDataError, RuntimeError, ValueError) as error:
        raise PDFTextError("The PDF could not be opened. Try another PDF file.") from error

    try:
        if document.is_encrypted:
            raise PDFTextError("Password-protected PDFs are not supported.")
        if document.page_count > MAX_PAGES:
            raise PDFTextError("The PDF has more than 100 pages and cannot be analyzed.")

        text = "\n".join(page.get_text("text") for page in document)
    except PDFTextError:
        raise
    except (RuntimeError, ValueError) as error:
        raise PDFTextError("Text could not be safely extracted from this PDF.") from error
    finally:
        document.close()

    if not text.strip():
        raise PDFTextError(
            "No selectable text was found. Scanned PDFs need OCR, which this MVP does not provide."
        )
    return text