import abc
from typing import Any, Optional

from src.apps.property.application.connection import ConnectionRepository
from src.utils.validator import AbstractValidation


class AbstractStrategy(abc.ABC):

    def __init__(
        self,
        validation: Optional[AbstractValidation],
        database_connection: Optional[ConnectionRepository]
    ):
        self.validation = validation
        self.database_connection = database_connection

    @abc.abstractmethod
    def _handle(self, request: Any):
        pass
