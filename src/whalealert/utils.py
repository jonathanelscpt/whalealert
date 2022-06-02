from datetime import datetime, timedelta


def ephoch_time(time: datetime) -> int:
    """
    Convert datetime to epoch seconds

    :param time: datetime obj
    :return: ephoch seconds
    """
    return int(time.timestamp())


def recent(mins: int) -> int:
    """
    Last X minutes in epoch time

    :param mins: minutes
    :return: epoch seconds
    """
    return ephoch_time(datetime.now() - timedelta(minutes=mins))
