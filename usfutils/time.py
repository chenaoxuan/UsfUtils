"""
Time related methods.
"""
import time

__all__ = [
    'get_time_str',
    'get_time_int',
    'get_time_asc'
]


def get_time_str() -> str:
    """

    :return:
    """
    return time.strftime('%Y%m%d_%H%M%S', time.localtime())


def get_time_int() -> int:
    """

    :return:
    """
    return int(time.time())


def get_time_asc() -> str:
    """
    e.g. 'Sat Jun 06 16:26:11 1998'.
    :return:
    """
    return time.asctime()
