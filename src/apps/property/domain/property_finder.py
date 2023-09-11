from typing import Dict, Any

from src.apps.property.application.finder import PropertyRepository


class PropertyFinder:

    def __init__(self, repository_finder: PropertyRepository):
        self.repository_finder = repository_finder

    def search(
        self,
        **kwargs
    ) -> Dict[str, Any]:
        return self.repository_finder.get(
            **kwargs
        )
