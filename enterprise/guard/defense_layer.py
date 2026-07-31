"""
GUARD DEFENSE LAYER — Maximum Protection
Aggressive validation, exponential backoff retries, circuit breakers, exhaustive logging.
"""
import time, math, random, logging
from typing import Any
from enterprise.core.abstract_interfaces import IGuardDefenseLayer

logger = logging.getLogger("enterprise.guard")
class EnterpriseDefense(IGuardDefenseLayer):
    def __init__(self):
        self.failure_counts = {}
        self.threshold = 3
    def validate_input(self, payload) -> bool:
        if payload is None:
            raise ValueError("NULL PAYLOAD — rejected by defense")
        if isinstance(payload, str) and len(payload) < 1:
            raise ValueError("EMPTY STRING — rejected")
        logger.info(f"VALIDATED: payload type={type(payload).__name__}")
        return True
    def retry_with_backoff(self, operation, max_attempts=5, base_delay=1.0) -> Any:
        for attempt in range(1, max_attempts + 1):
            try:
                self.validate_input(operation)
                result = operation() if callable(operation) else operation
                logger.info(f"SUCCESS on attempt {attempt}")
                return result
            except Exception as e:
                delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.5)
                logger.error(f"FAIL attempt {attempt}: {e} | retry in {delay:.2f}s")
                if attempt == max_attempts:
                    raise RuntimeError(f"MAX RETRIES EXHAUSTED: {e}")
                time.sleep(delay)
    def circuit_breaker_check(self, service_name: str) -> bool:
        count = self.failure_counts.get(service_name, 0)
        if count >= self.threshold:
            logger.critical(f"CIRCUIT BREAKER OPEN: {service_name} — blocking calls")
            return False
        return True
