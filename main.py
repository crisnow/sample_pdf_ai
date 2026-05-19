from pdf_extractor import extract_text_from_pdf
from ai_extractor import extract_invoice_data
from summary import generate_summary


def main():
    pdf_path = "sample_data/sample_invoice.pdf"

    print("Reading PDF...")
    pdf_text = extract_text_from_pdf(pdf_path)
    print(pdf_text)

    if not pdf_text:
        print("No text extracted from PDF.")
        return

    print("Extracting structured data with AI...")
    invoice_data = extract_invoice_data(pdf_text)

    print("\nStructured Data:")
    print(invoice_data.model_dump_json(indent=2))

    print("\n3-Line Summary:")
    print(generate_summary(invoice_data))


if __name__ == "__main__":
    main()
