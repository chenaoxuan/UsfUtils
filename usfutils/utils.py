"""
Other more basic operations.
"""
import time


def get_time_str():
    return time.strftime('%Y%m%d_%H%M%S', time.localtime())
