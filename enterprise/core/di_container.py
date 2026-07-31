"""
DEPLOYMENT CONTAINER — Dependency Injection + Service Registry
Builds services with injected dependencies (defense, cache, queue, adapter)
"""
from .abstract_interfaces import IExamDataExtractor, IRevisionPackBuilder, IPracticeWorkbookGenerator, IGuardDefenseLayer, ICacheRegionLayer
from typing import Dict, Any

class EnterpriseContainer:
    def __init__(self):
        self._services: Dict[str, Any] = {}
        self._dependencies: Dict[str, Any] = {}
    def register_dependency(self, name: str, instance: Any) -> None:
        self._dependencies[name] = instance
    def register_service(self, name: str, factory: callable, *deps) -> None:
        instances = [self._dependencies[d] for d in deps]
        self._services[name] = factory(*instances)
    def resolve(self, name: str) -> Any:
        if name not in self._services:
            raise KeyError(f"Service '{name}' not registered")
        return self._services[name]

# Global registry for multi-region deployment
GLOBAL_REGISTRY = EnterpriseContainer()
