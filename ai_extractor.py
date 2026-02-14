import json
from openai import OpenAI
from models import InvoiceData


# Create client (make sure OPENAI_API_KEY is set in your environment)
client = OpenAI()


def extract_invoice_data(text: str) -> InvoiceData:
    """
    Sends invoice text to the LLM and extracts structured data.
    """

    prompt = f"""
    Extract the following fields from this logistics invoice:

    - invoice_number
    - total_amount
    - currency
    - due_date
    - shipper
    - consignee

    Return valid JSON only.

    Invoice Text:
    {text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You extract structured data from logistics invoices."},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )

        content = response.choices[0].message.content

        data = json.loads(content)

        return InvoiceData(**data)

    except Exception as e:
        print(f"AI extraction error: {e}")
        return InvoiceData()
