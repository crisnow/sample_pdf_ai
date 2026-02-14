📦 Smart Logistics Email Summarizer (Prototype)
🚀 Overview

This project is a prototype of an AI-powered email automation tool for the logistics industry.

The system:
Reads a logistics invoice (PDF)
Extracts key structured data using an LLM API
Validates the extracted data
Generates a concise 3-line operational summary

The goal is to demonstrate how AI can automate invoice processing and reduce manual workload in logistics operations.

🏗 Architecture

The project follows a modular structure with clear separation of responsibilities:

project/
│
├── main.py              # Application entry point

├── pdf_extractor.py     # Extracts text from PDF documents

├── ai_extractor.py      # Sends text to LLM and parses structured output

├── summary.py           # Generates operational 3-line summary

├── models.py            # Pydantic data models

└── sample_data/
    └── invoice.pdf
