# Invoice AI Extractor

An AI-assisted prototype that converts logistics invoices in PDF format into clean, structured data and a concise operational summary.

Built with FastAPI, `pdfplumber`, Pydantic, and Google Gemini.

## What it does

1. Accepts a text-based invoice PDF through a simple browser interface or the command line.
2. Extracts the document text with `pdfplumber`.
3. Uses Gemini to identify key invoice information.
4. Validates the response with a Pydantic model.
5. Returns the structured data and a three-line operational summary.

### Extracted fields

| Field | Description |
| --- | --- |
| `invoice_number` | Supplier invoice reference |
| `total_amount` | Invoice total |
| `currency` | Currency code or label |
| `due_date` | Payment due date |
| `shipper` | Originating party |
| `consignee` | Receiving party |

## Quick start

### Prerequisites

- Python 3.10 or later
- A Google Gemini API key

### Install

```bash
git clone <your-repository-url>
cd sample_pdf_ai

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

> Keep `.env` private. Do not commit API keys to version control.

### Run the web app

```bash
uvicorn api:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) and upload a PDF invoice. If port 8000 is already in use, choose another port:

```bash
uvicorn api:app --reload --port 8001
```

### Run the command-line example

```bash
python main.py
```

This processes `sample_data/sample_invoice.pdf` and prints the extracted JSON plus the operational summary.

## API

### `POST /upload-invoice`

Upload a PDF using multipart form data with the field name `file`.

```bash
curl -X POST http://127.0.0.1:8000/upload-invoice \
  -F "file=@sample_data/sample_invoice.pdf"
```

Example response:

```json
{
  "structured_data": {
    "invoice_number": "INV-2026-001",
    "total_amount": 1250.0,
    "currency": "EUR",
    "due_date": "2026-12-15",
    "shipper": "Example Logistics GmbH",
    "consignee": "Example Customer Ltd"
  },
  "summary_lines": [
    "Invoice INV-2026-001 issued for 1250.0 EUR.",
    "Due date: 2026-12-15.",
    "Shipper: Example Logistics GmbH | Consignee: Example Customer Ltd."
  ]
}
```

## Project structure

```text
.
├── api.py               # FastAPI upload endpoint and web-app entry point
├── main.py              # Command-line demonstration
├── ai_extractor.py      # Gemini prompting, parsing, and model mapping
├── pdf_extractor.py     # PDF text extraction helper
├── summary.py           # Three-line operational summary formatter
├── models.py            # Pydantic invoice schema
├── index.html           # Single-page upload interface
├── sample_data/         # Example invoices
└── requirements.txt     # Python dependencies
```

## Current limitations

- The extractor is designed for **digital, text-based PDFs**. Scanned invoices need OCR before extraction.
- Extraction accuracy depends on invoice layout and the model response; review important financial data before acting on it.
- Uploads are currently written to `temp.pdf`, so this prototype should not be used for concurrent or production workloads without per-request temporary-file handling.
- There is no authentication, persistence, or audit trail yet.

## Deployment

The included `Procfile` starts the service with:

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

For production, configure the API key as a platform secret, restrict CORS to trusted origins, and add robust validation, logging, secure upload handling, and OCR support as needed.
