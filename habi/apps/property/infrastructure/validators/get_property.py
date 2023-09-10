import abc

from habi.apps.property.domain.models.models import ParamsProperty
from habi.apps.property.infrastructure.constants import STATUS_INVALID
from habi.utils import loggers
from habi.utils.exceptions import ValidationError
from habi.utils.validator import AbstractValidation

logger = loggers.setup_logger(logger_name=__name__)


class GetPropertyValidation(AbstractValidation):

    @abc.abstractmethod
    def run(self, request: ParamsProperty) -> None:
        pass


class ValidateState(GetPropertyValidation):

    def run(self, request: ParamsProperty) -> None:
        state = request.state
        if state and state[0] in STATUS_INVALID:
            msg = 'This status can not be filtered'
            logger.info(msg)
            raise ValidationError(msg)
