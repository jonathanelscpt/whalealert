from datetime import datetime


def ephoch_time(time: datetime) -> int:
    return int(time.timestamp())
