from typing import Optional, Union
from pydantic import BaseModel

class InvoiceData(BaseModel):
    invoice_number: Optional[str] = None
    total_amount: Optional[Union[str, float]] = None
    currency: Optional[str] = None
    due_date: Optional[str] = None
    shipper: Optional[str] = None
    consignee: Optional[str] = None