"""
Operations related to paths, files, directories, etc.
"""
import os
from typing import Union, Generator

from .time import get_time_str

__all__ = [
    'mkdir_and_exist',
    'mkdir_and_rename',
    'scandir'
]


def mkdir_and_exist(path: str) -> None:
    """
    Create a new directory with the name 'path'. If it already exists, do nothing.
    :param path: The name of the new directory.
    :return: None
    """
    if not isinstance(path, str):
        raise TypeError("Parameter 'path' must be a string.")
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError as e:
            raise Exception(f"Failed to create the directory: {e}.")
    else:
        print(f"Directory '{path}' already exists, no change.")


def mkdir_and_rename(path: str) -> None:
    """
    If directory 'path' already exists, rename it with timestamp; else, create a new one.
    :param path: The name of the new directory.
    :return: None
    """
    if not isinstance(path, str):
        raise TypeError("Parameter 'path' must be a string.")
    if os.path.exists(path):
        try:
            new_path = path + '_archived_' + get_time_str()
            os.rename(path, new_path)
            print(f"Directory already exists. Rename it to {new_path}.", flush=True)
        except OSError as e:
            raise Exception(f"Failed to rename the directory: {e}.")
    try:
        os.makedirs(path)
    except OSError as e:
        raise Exception(f"Failed to create the directory: {e}.")


def scandir(path: str, suffix: Union[str, tuple] = None, recursive: bool = False, full_path: bool = False) -> Generator:
    """
    Scan a directory and retrieve all its sub files.
    :param path: Directory to retrieve.
    :param suffix: Retrieve files with specific suffixes, such as '.png' or ('.png','.jpg').
    :param recursive: Whether to recursively retrieve subdirectories of 'path'.
    :param full_path: Whether to return the absolute path of the retrieval result.
    :return: A generator that iterates through it to obtain search results.
    """
    if not isinstance(path, str):
        raise TypeError("Parameter 'path' must be a string.")
    if (suffix is not None) and not isinstance(suffix, (str, tuple)):
        raise TypeError("Parameter 'suffix' must be a string or tuple of strings.")
    root = path

    def _scandir(path, suffix, recursive):
        for entry in os.scandir(path):
            if not entry.name.startswith('.') and entry.is_file():
                if full_path:
                    return_path = entry.path
                else:
                    return_path = os.path.relpath(entry.path, root)

                if suffix is None:
                    yield return_path
                elif return_path.endswith(suffix):
                    yield return_path
            else:
                if recursive:
                    yield from _scandir(entry.path, suffix=suffix, recursive=recursive)
                else:
                    continue

    return _scandir(path, suffix=suffix, recursive=recursive)
