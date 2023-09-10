from marshmallow import Schema, fields, validate


class PropertySerializer(Schema):
    address = fields.Str(required=True)
    city = fields.Str(required=True)
    status = fields.Str(required=True)
    price = fields.Int(required=True)
    description = fields.Str(required=True)


class OutListPropertySerializer(Schema):
    response_data = fields.List(
        fields.Nested(PropertySerializer), required=False
    )


class IngressPropertySerializer(Schema):
    state = fields.String(validate=validate.OneOf(
        ['comprando', 'comprado', 'pre_venta', 'en_venta', 'vendido']
    ), required=False)
    year = fields.Str(required=False)
    city = fields.Str(required=False)
