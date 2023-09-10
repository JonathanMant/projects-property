import abc
from typing import Any


class AbstractValidation(abc.ABC):

    @abc.abstractmethod
    def run(self, request: Any) -> None:
        raise
