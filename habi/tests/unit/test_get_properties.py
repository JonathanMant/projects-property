from typing import List

import pytest

from habi.apps.property.application.connection import ConnectionRepository
from habi.apps.property.domain.models.models import Connection
from habi.apps.property.domain.property_finder import PropertyFinder
from habi.apps.property.infrastructure.finder_mysql import FinderPropertyHabi
from habi.utils.exceptions import ValidationError


class FakeConnectionRepository(ConnectionRepository):

    def get_connection(self, **kwargs) -> Connection:
        pass

    def get_data(self, **kwargs) -> List:
        query = kwargs.get('query')

        if 'p.year' in query:
            return [
                (
                    'calle 23 #45-67q',
                    'bogota',
                    'pre_venta',
                    120000000,
                    'Hermoso apartamento en el centro de la ciudad'
                )
            ]
        return [
            (
                'calle 23 #45-67',
                'bogota',
                'pre_venta',
                120000000,
                'Hermoso apartamento en el centro de la ciudad'
            ),
            (
                'carrera 100 #15-90',
                'bogota',
                'en_venta',
                350000000,
                'Amplio apartamento en conjunto cerrado'
            ),
            (
                'diagonal 23 #28-21',
                'bogota',
                'vendido',
                270000000,
                'Apartamento con hermosas vistas'
            )
        ]


class TestGetProperties:

    def test_get_properties_with_params_successful(self):
        params = {
            'year': ['2000'],
            'city': ['bogota'],
            'state': ['pre_venta']
        }

        response = PropertyFinder(
            repository_finder=FinderPropertyHabi(
                database_connection=FakeConnectionRepository()
            )
        ).search(
            **params
        )
        data_response = response.get('response_data')
        assert data_response
        assert data_response == [{
            'address': 'calle 23 #45-67q',
            'city': 'bogota',
            'status': 'pre_venta',
            'price': 120000000,
            'description': 'Hermoso apartamento en el centro de la ciudad'
        }]

    def test_get_properties_without_params_successful(self):
        params = {}

        response = PropertyFinder(
            repository_finder=FinderPropertyHabi(
                database_connection=FakeConnectionRepository()
            )
        ).search(
            **params
        )
        data_response = response.get('response_data')
        assert data_response
        assert data_response == [
            {
                'address': 'calle 23 #45-67',
                'city': 'bogota',
                'status': 'pre_venta',
                'price': 120000000,
                'description': 'Hermoso apartamento en el centro de la ciudad'
            },
            {
                'address': 'carrera 100 #15-90',
                'city': 'bogota',
                'status': 'en_venta',
                'price': 350000000,
                'description': 'Amplio apartamento en conjunto cerrado'
            },
            {
                'address': 'diagonal 23 #28-21',
                'city': 'bogota',
                'status': 'vendido',
                'price': 270000000,
                'description': 'Apartamento con hermosas vistas'
            }
        ]

    def test_get_properties_a_status_incorrect_error(self):
        params = {
            'state': ['comprado']
        }
        with pytest.raises(ValidationError):
            response = PropertyFinder(
                repository_finder=FinderPropertyHabi(
                    database_connection=FakeConnectionRepository()
                )
            ).search(
                **params
            )
            assert not response.get('return')
