from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import marshmallow

from habi.apps.property.domain.property_finder import PropertyFinder
from habi.apps.property.domain.serializer import (
    OutListPropertySerializer, IngressPropertySerializer
)
from habi.apps.property.infrastructure.connection_mysql import ConnectionMysql
from habi.apps.property.infrastructure.finder_mysql import FinderPropertyHabi
import json

from habi.utils import loggers
from habi.utils.exceptions import ValidationError

logger = loggers.setup_logger(logger_name=__name__)


class MiManejador(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith('/get_properties'):
            try:
                parsed_url = urlparse(self.path)
                params = parse_qs(parsed_url.query)
                params = IngressPropertySerializer().load(
                    {key: value[0] for key, value in params.items()}
                )
                response = PropertyFinder(
                    repository_finder=FinderPropertyHabi(
                        database_connection=ConnectionMysql()
                    )
                ).search(
                    **params
                )
                response = OutListPropertySerializer().load(response)
                message = json.dumps(response.get('response_data'))
                self.send_response(200)
            except ValidationError as v:
                message = f'There is a error with :: {v}'
                logger.info(message)
                self.send_response(400)
            except marshmallow.exceptions.ValidationError as m:
                message = f'There is a error with serializer:: {m}'
                logger.info(message)
                self.send_response(400)
            except Exception as e:
                message = f'There is a error with :: {e}'
                logger.info(message)
                self.send_response(500)
        else:
            self.send_response(404)
            message = "Not found page"

        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
