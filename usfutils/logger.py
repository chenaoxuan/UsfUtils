"""
Log management.
"""
import os
import logging
from .dist import get_dist_info
from .time import get_time_str

__all__ = [
    'get_root_logger',
    'get_env_info'
]

initialized_logger = {}


def get_root_logger(log_path: str, logger_name: str = 'usfutils', logger_level=logging.INFO,
                    ) -> logging.Logger:
    """
    Get a simple and easy-to-use logger.
    Note that the logger level is only set to INFO in processes with rank=0, and to ERROR in other processes to keep them silent.
    :param log_path: The log file directory. The log file will be created in this directory with time.
    :param logger_name: The logger name.
    :param logger_level: The level of the logger,
    :return:
    """
    if log_path is None:
        raise ValueError("logger_path cannot be None")
    if not os.path.exists(log_path):
        raise FileNotFoundError(f"Logger path '{log_path}' does not exist")
    logger_file = os.path.join(log_path, f"Log_{get_time_str()}.txt")
    logger = logging.getLogger(logger_name)
    if logger_name in initialized_logger:
        return logger
    format_str = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(format_str)
    logger.addHandler(stream_handler)
    rank, _ = get_dist_info()
    if rank != 0:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logger_level)
        file_handler = logging.FileHandler(logger_file, mode='w', encoding='utf-8')
        file_handler.setFormatter(format_str)
        file_handler.setLevel(logger_level)
        logger.addHandler(file_handler)
        logger.info(get_env_info())
    initialized_logger[logger_name] = True
    return logger


def get_env_info() -> str:
    """
    Get information about Python and some important libraries and return them.
    :return: msg
    """
    msg = r"""
     ______                   __   __                 __      __
    / ____/____   ____   ____/ /  / /   __  __ _____ / /__   / /
   / / __ / __ \ / __ \ / __  /  / /   / / / // ___// //_/  / /
  / /_/ // /_/ // /_/ // /_/ /  / /___/ /_/ // /__ / /<    /_/
  \____/ \____/ \____/ \____/  /_____/\____/ \___//_/|_|  (_)
    """
    import sys
    msg += f'\nPython:{sys.version}'
    from usfutils.version import __version__
    msg += f'\nUsfUtils:{__version__}'
    try:
        import torch
        msg += f'\nPytorch:{torch.__version__}'
    except:
        pass
    try:
        import torchvision
        msg += f'\nTorchVision:{torchvision.__version__}'
    except:
        pass

    return msg
