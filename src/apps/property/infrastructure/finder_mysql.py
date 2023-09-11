from typing import Optional, Dict, Any

from src.apps.property.application.connection import ConnectionRepository
from src.apps.property.application.finder import PropertyRepository
from src.apps.property.domain.models.models import ParamsProperty
from src.apps.property.infrastructure.strategy.get_property import GetProperty
from src.apps.property.infrastructure.validators.get_property import (
    ValidateState
)
from src.utils import loggers

logger = loggers.setup_logger(logger_name=__name__)


class FinderPropertyHabi(PropertyRepository):

    def __init__(
        self,
        *,
        database_connection: ConnectionRepository
    ):
        self.database_connection = database_connection

    def get(
        self,
        *,
        year: Optional[int] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:

        strategy = GetProperty(
            validation=ValidateState(),
            database_connection=self.database_connection
        )

        response = strategy.get_property(
            request=ParamsProperty(
                year=year,
                city=city,
                state=state
            )
        )

        return {'response_data': response}
