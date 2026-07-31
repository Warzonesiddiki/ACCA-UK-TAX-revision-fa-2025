"""
HTML BUILDER SERVICE — Microservice with Injection
Integrates examiner reports, questions, and gamification into master HTML.
"""
import re
from enterprise.core.abstract_interfaces import IRevisionPackBuilder, ExamKitContract
from enterprise.guard.defense_layer import EnterpriseDefense
from enterprise.adapters.format_adapter import FormatAdapter

class HtmlBuilderService(IRevisionPackBuilder):
    def __init__(self, defense: EnterpriseDefense, adapter: FormatAdapter):
        self.defense = defense
        self.adapter = adapter
    def build_html(self, data_contract: ExamKitContract, examiner_feed: list, plugin_context: dict) -> str:
        self.defense.validate_input(data_contract)
        with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
            html = f.read()
        # Insert examiner feedback blocks (simulated batch insertion)
        for item in examiner_feed:
            block = f'<div class="callout callout-examiner"><div class="callout-title">📋 EXAMINER FEEDBACK — PDF p.{item.get("page", "?")}</div><p>{item.get("content", "")}</p></div>'
            # Find insertion point near Section C or relevant part
            html = html.replace('<div class="card">', block + '<div class="card">', 1)
        # Apply plugin extensions
        for ext_name, handler in plugin_context.get("extensions", {}).items():
            html = handler(html)
        return html
    def inject_examiner_feedback(self, html_content: str, feedback_items: list, defense_layer: any) -> str:
        defense_layer.validate_input(feedback_items)
        return self.build_html(ExamKitContract("TX_Exam_Kit_FA25.pdf"), feedback_items, {})
