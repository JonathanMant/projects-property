import abc

from src.apps.property.domain.models.models import ParamsProperty
from src.apps.property.infrastructure.constants import STATUS_INVALID
from src.utils import loggers
from src.utils.exceptions import ValidationError
from src.utils.validator import AbstractValidation

logger = loggers.setup_logger(logger_name=__name__)


class GetPropertyValidation(AbstractValidation):

    @abc.abstractmethod
    def run(self, request: ParamsProperty) -> None:
        pass


class ValidateState(GetPropertyValidation):

    def run(self, request: ParamsProperty) -> None:
        state = request.state
        if state and state in STATUS_INVALID:
            msg = 'This status can not be filtered'
            logger.info(msg)
            raise ValidationError(msg)
