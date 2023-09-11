from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class PropertyRepository(ABC):

    @abstractmethod
    def get(
        self,
        *,
        year: Optional[int] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Obtain a property with all information
        """
        pass
