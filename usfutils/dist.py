"""
Distributed (mainly Pytorch) management.
"""
import functools
from typing import Tuple

__all__ = [
    'get_dist_info',
    'master_only'
]


def get_dist_info() -> Tuple[int, int]:
    """

    :return:
    """
    try:
        import torch.distributed as dist
        if dist.is_available():
            initialized = dist.is_initialized()
        else:
            initialized = False
        if initialized:
            rank = dist.get_rank()
            world_size = dist.get_world_size()
        else:
            rank = 0
            world_size = 1
        return rank, world_size
    except ImportError:
        return 0, 1


def master_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rank, _ = get_dist_info()
        if rank == 0:
            return func(*args, **kwargs)

    return wrapper
