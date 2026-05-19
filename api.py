from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pdfplumber
from ai_extractor import extract_invoice_data
from summary import generate_summary
import os

app = FastAPI()

# allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def serve_index():
    """Serve the index.html file"""
    return FileResponse("index.html", media_type="text/html")

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


@app.post("/upload-invoice")
async def upload_invoice(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    # save temporarily
    with open("temp.pdf", "wb") as f:
        f.write(pdf_bytes)

    text = extract_text_from_pdf("temp.pdf")

    result = extract_invoice_data(text)
    print("summary: ")
    print(result)

    summary = generate_summary(result)
    summary_lines = [line.strip() for line in summary.split('\n') if line.strip()]
    print("summary_lines")
    print(summary_lines)

    return {
        "structured_data": result.model_dump(),
        "summary_lines": summary_lines
    }