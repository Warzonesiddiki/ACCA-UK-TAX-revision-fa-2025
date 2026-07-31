"""
EXAM FORMAT PLUGIN — Extensible Business Logic
Allows adding new exam formats (FA2026, international, etc.) without core changes.
"""
class ExamFormatPlugin:
    def __init__(self, version: str = "FA2025"):
        self.version = version
        self.extensions = {}
    def register_extension(self, name: str, handler: callable):
        self.extensions[name] = handler
    def apply(self, data: dict, extension: str = "base") -> dict:
        if extension in self.extensions:
            return self.extensions[extension](data)
        return data
