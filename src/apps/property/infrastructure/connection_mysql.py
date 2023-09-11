import os
from typing import List

import mysql.connector

from src.apps.property.application.connection import (
    ConnectionRepository
)

from src.apps.property.domain.models.models import Connection


class ConnectionMysql(ConnectionRepository):

    def __init__(self):
        self.connection = None

    def connection_database(self, **kwargs) -> None:
        config = {
            'user': os.getenv('DATA_USER_MYSQL'),
            'password': os.getenv('DATA_PASS_MYSQL'),
            'host': os.getenv('DATA_HOST_MYSQL'),
            'database': os.getenv('DATA_NAME_MYSQL'),
            'port': os.getenv('DATA_PORT_MYSQL')
        }

        self.connection = mysql.connector.connect(**config)

    def get_connection(self) -> Connection:
        self.connection_database()
        return Connection(
            cursor=self.connection.cursor()
        )

    def __exit__(self, *args):
        self.exit_db()

    def exit_db(self) -> None:
        self.connection.close()

    def get_data(self, **kwargs) -> List:
        connection = self.get_connection()
        connection.cursor.execute(kwargs.get('query'))
        return connection.cursor.fetchall()
