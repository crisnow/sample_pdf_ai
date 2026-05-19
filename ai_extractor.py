import os
import json
import re
from google import genai
from models import InvoiceData
from dotenv import load_dotenv

load_dotenv()


def clean_json(text: str) -> str:
    """
    Removes markdown fences and extra noise from LLM output.
    """
    text = text.strip()

    # remove ```json or ``` wrappers
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    return text.strip()


def extract_invoice_data(text: str) -> InvoiceData:
    """
    Sends invoice text to Gemini and extracts structured invoice data.
    """

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY is missing in environment variables")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-flash-lite-latest")

    prompt = f"""
You are a strict JSON extraction engine.

Extract invoice data from the text below.

Return ONLY valid JSON.
No markdown.
No explanations.
No backticks.

Schema:
{{
  "invoice_number": string or null,
  "total_amount": number or null,
  "currency": string or null,
  "due_date": string or null,
  "shipper": string or null,
  "consignee": string or null
}}

TEXT:
{text}
"""

    try:
        response = model.generate_content(prompt)

        raw = response.text or ""

        print("\nRAW RESPONSE:")
        print(raw)

        cleaned = clean_json(raw)

        if not cleaned:
            raise ValueError("Empty response from Gemini")

        data = json.loads(cleaned)

        # Map safely into Pydantic model
        invoice = InvoiceData(
            invoice_number=data.get("invoice_number"),
            total_amount=data.get("total_amount"),
            currency=data.get("currency"),
            due_date=data.get("due_date"),
            shipper=data.get("shipper"),
            consignee=data.get("consignee"),
        )

        return invoice

    except Exception as e:
        print(f"AI extraction error: {e}")
        return InvoiceData()