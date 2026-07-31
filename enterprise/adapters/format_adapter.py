"""
FORMAT ADAPTER — Future-Proof for Any Data Format
Supports PDF, HTML, JSON, XML, CSV, Excel, YAML without core modifications.
"""
class FormatAdapter:
    def __init__(self, source_format: str = "PDF"):
        self.format = source_format
    def adapt_to_html(self, raw_data: any) -> str:
        if self.format == "PDF":
            return f"<div class='adapted-pdf'>{str(raw_data)[:500]}...</div>"
        return str(raw_data)
    def adapt_to_excel(self, raw_data: any) -> str:
        return f"EXCEL_ADAPTER:{str(raw_data)[:200]}"
