"""
Other more basic operations.
"""
import time

__all__ = [
    'get_time_str'
]


def get_time_str():
    return time.strftime('%Y%m%d_%H%M%S', time.localtime())


def set_seed_everything():
    pass
    # todo
