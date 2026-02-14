from pydantic import BaseModel
from typing import Optional


class InvoiceData(BaseModel):
    invoice_number: Optional[str] = None
    total_amount: Optional[str] = None
    currency: Optional[str] = None
    due_date: Optional[str] = None
    shipper: Optional[str] = None
    consignee: Optional[str] = None
