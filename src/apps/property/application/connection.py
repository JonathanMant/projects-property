from abc import ABC, abstractmethod
from typing import List

from src.apps.property.domain.models.models import Connection


class ConnectionRepository(ABC):

    @abstractmethod
    def get_connection(
        self,
        **kwargs
    ) -> Connection:
        """
        Get connection with the database
        """
        pass

    @abstractmethod
    def get_data(
        self,
        **kwargs
    ) -> List:
        """
        Save changes in the database
        """
        pass
