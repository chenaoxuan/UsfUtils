"""
Used to automatically load modules from configuration files, such as models, dataloaders, etc.
"""

import importlib
from typing import Callable
from .dict import UsfDict

__all__ = [
    'instantiate_from_config',
    'get_obj_from_str',
]


def get_obj_from_str(string: str, reload: bool = False) -> Callable:
    """
    Import object from the complete module path string.
    :param string: A complete object string path.
    :param reload: Reload the module to support code hot updates.
    :return: A callable object.
    """
    if string is None:
        raise TypeError("string can not be None.")
    module, cls = string.rsplit(sep='.', maxsplit=1)
    if reload:
        module_imp = importlib.import_module(module)
        importlib.reload(module_imp)
    return getattr(importlib.import_module(module), cls)


def instantiate_from_config(config: UsfDict):
    if "target" not in config:
        raise KeyError("Expected key `target` to instantiate.")
    return get_obj_from_str(config["target"])(**config.get("params", dict()))
