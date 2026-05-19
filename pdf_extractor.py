import pdfplumber


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts all text from a PDF file.
    Works for digital PDFs (not scanned images).
    """
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                # print(page_text)
                if page_text:
                    text += page_text + "\n"
      

        return text.strip()

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""


extract_text_from_pdf("sample_data/sample_invoice.pdf")
