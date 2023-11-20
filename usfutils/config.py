import io
import os
import sys
import yaml
from shutil import copyfile

from .dist import master_only
from .utils import get_time_asc

__all__ = [
    'UsfConfig'
]


class UsfConfig():
    """
    UsfConfig primary class.
    Currently, only yaml files with dict type after loading are supported.
    """

    @staticmethod
    def load(path: str):
        if path is None:
            raise TypeError("path can not be None.")
        print(os.path.abspath(path))
        with io.open(os.path.abspath(path), 'r', encoding='utf-8') as f:
            obj = yaml.safe_load(f)
        return obj

    @staticmethod
    def to_yaml(obj: dict, path: str):
        if not isinstance(obj, dict):
            raise TypeError("UsfConfig now only support dict")
        if path is None:
            raise TypeError("path can not be None.")
        with io.open(os.path.abspath(path), 'w', encoding='utf-8') as f:
            yaml.dump(obj, path)

    @staticmethod
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

    @staticmethod
    def dict_to_str(opt, indent_level=1):
        """
        Indent dict according to hierarchical relationships and convert it to str.
        :param opt:
        :param indent_level:
        :return:
        """
        msg = '\n'
        for k, v in opt.items():
            if isinstance(v, dict):
                msg += ' ' * (indent_level * 2) + k + ':['
                msg += UsfConfig.dict_to_str(v, indent_level + 1)
                msg += ' ' * (indent_level * 2) + ']\n'
            else:
                msg += ' ' * (indent_level * 2) + k + ': ' + str(v) + '\n'
        return msg
