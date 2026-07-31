"""
ENTREPRISE CORE — ABSTRACT INTERFACES (Maximum Abstraction)
Pattern: Abstract Base Class | Dependency Injection | Strategy Engine
Future-proof: Any data source / output format can be plugged without core change.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Protocol
from dataclasses import dataclass
import logging

logger = logging.getLogger("enterprise.core")

@dataclass(frozen=True)
class ExamKitContract:
    """Immutable contract for exam kit data — future-proof against format changes."""
    source_path: str
    format_version: str = "FA2025"
    total_pages: int = 684
    region_token: str = "GLOBAL"
    checksum_hash: Optional[str] = None

class IExamDataExtractor(ABC):
    @abstractmethod
    def extract_questions(self, contract: ExamKitContract, region: str = "GLOBAL") -> Dict[str, Any]:
        pass
    @abstractmethod
    def extract_examiner_reports(self, page_range: tuple, max_retries: int = 5) -> list:
        pass

class IRevisionPackBuilder(ABC):
    @abstractmethod
    def build_html(self, data_contract: ExamKitContract, examiner_feed: list, plugin_context: Dict) -> str:
        pass
    @abstractmethod
    def inject_examiner_feedback(self, html_content: str, feedback_items: list, defense_layer: Any) -> str:
        pass

class IPracticeWorkbookGenerator(ABC):
    @abstractmethod
    def generate_section_c_workbook(self, contract: ExamKitContract, exam_data: Dict, region: str) -> str:
        pass

class IGuardDefenseLayer(ABC):
    @abstractmethod
    def validate_input(self, payload: Any) -> bool:
        pass
    @abstractmethod
    def retry_with_backoff(self, operation: callable, max_attempts: int = 5, base_delay: float = 1.0) -> Any:
        pass
    @abstractmethod
    def circuit_breaker_check(self, service_name: str) -> bool:
        pass

class ICacheRegionLayer(ABC):
    @abstractmethod
    def get(self, key: str, region: str = "global") -> Any:
        pass
    @abstractmethod
    def set(self, key: str, value: Any, ttl: int = 3600, region: str = "global") -> bool:
        pass

# Strategy Engine — decouples business logic from execution
class BuildStrategyEngine:
    def __init__(self, strategy_map: Dict[str, Any]):
        self._map = strategy_map
        self._current = None
    def select(self, strategy_key: str) -> None:
        if strategy_key not in self._map:
            raise ValueError(f"Unknown strategy: {strategy_key}")
        self._current = self._map[strategy_key]
        logger.info(f"Strategy selected: {strategy_key}")
    def execute(self, *args, **kwargs) -> Any:
        if not self._current:
            raise RuntimeError("No strategy selected")
        return self._current.execute(*args, **kwargs)
