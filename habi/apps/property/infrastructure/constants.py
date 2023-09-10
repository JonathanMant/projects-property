import os

STATUS_INVALID = os.getenv(
    'STATUS_INVALID',
    'comprando,comprado'
).split(',')
