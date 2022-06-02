from typing import Union
from datetime import datetime


def hex_from_bytes_or_string(x: Union[bytes, str]):
    return x if type(x) is str else x.hex()


def ephoch_time(time: datetime):
    return int(time.timestamp())
