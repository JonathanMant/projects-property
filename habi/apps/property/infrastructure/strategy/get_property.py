import abc
from typing import Dict, List

from habi.apps.property.domain.models.models import ParamsProperty
from habi.utils.strategy import AbstractStrategy


class AbstractPropertyStrategy(AbstractStrategy):

    @abc.abstractmethod
    def _handle(self, request: ParamsProperty):
        pass


class GetProperty(AbstractPropertyStrategy):

    def _handle(self, request: ParamsProperty) -> List:
        query_where = self.get_query(
            params={
                'p.year': request.year,
                'p.city': request.city,
                's.name': request.state
            }
        )
        query = (
            "SELECT p.address, p.city, s.name , p.price, p.description "
            "FROM property p left join ("
            "select sh.property_id, sh.status_id from status_history sh "
            "where sh.update_date = ("
            "select max(sh2.update_date) from status_history sh2 "
            "where sh2.property_id = sh.property_id) "
            "group by sh.property_id) as p2 "
            f"on p.id = p2.property_id "
            f"left join status s on p2.status_id=s.id{query_where} "
            f"and s.name in ('pre_venta', 'en_venta', 'vendido')"
        )

        response = self.database_connection.get_data(
            query=query
        )

        properties_list = [
            {'address': house[0], 'city': house[1], 'status': house[2],
             'price': house[3], 'description': house[4]}
            for house in response
            if all(house)
        ]

        return properties_list

    @staticmethod
    def get_query(*, params: Dict) -> str:
        query_values = [
            f'{key}="{value}"'
            for key, value in params.items()
            if value
        ]
        if not query_values:
            return ''
        sql_where = ' and '.join(query_values)
        return f' where {sql_where}'

    def get_property(self, *, request: ParamsProperty) -> List:
        self.validation.run(request=request)
        return self._handle(request=request)
