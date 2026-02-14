from models import InvoiceData


def generate_summary(data: InvoiceData) -> str:
    """
    Generates a clean 3-line operational summary.
    """

    return (
        f"Invoice {data.invoice_number or 'N/A'} "
        f"issued for {data.total_amount or 'N/A'} {data.currency or ''}.\n"
        f"Due date: {data.due_date or 'N/A'}.\n"
        f"Shipper: {data.shipper or 'N/A'} | "
        f"Consignee: {data.consignee or 'N/A'}."
    )
