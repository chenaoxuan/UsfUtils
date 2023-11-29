import io
import os
import sys
import yaml
from shutil import copyfile
from typing import Union
from .dist import master_only
from .time import get_time_asc
from .dict import UsfDict

__all__ = [
    'load_yaml',
    'dict_to_yaml',
    'copy_opt_file'
]


def load_yaml(path: str) -> UsfDict:
    if path is None:
        raise TypeError("path can not be None.")
    print(os.path.abspath(path))
    with io.open(os.path.abspath(path), 'r', encoding='utf-8') as f:
        obj = yaml.safe_load(f)
    obj = UsfDict(obj)
    return obj


def dict_to_yaml(obj: Union[UsfDict, dict], path: str):
    if not isinstance(obj, dict):
        raise TypeError("UsfConfig now only support dict")
    if path is None:
        raise TypeError("path can not be None.")
    obj = dict(obj)
    with open(os.path.abspath(path), 'w', encoding='utf-8') as f:
        yaml.dump(obj, f)


@master_only
def copy_opt_file(file_path: str, experiments_path: str) -> None:
    """
    Copy the yaml file to the experiment root
    :param file_path: Configuration file yaml.
    :param experiments_path: Experimental Path.
    :return:
    """
    if file_path is None or experiments_path is None:
        raise TypeError("path can not be None.")
    cmd = ' '.join(sys.argv)
    filename = os.path.join(experiments_path, os.path.basename(file_path))
    copyfile(file_path, filename)
    with open(filename, 'r+') as f:
        lines = f.readlines()
        lines.insert(0, f'# Generate Time: {get_time_asc()}\n# Command: {cmd}\n\n')
        f.seek(0)
        f.writelines(lines)
