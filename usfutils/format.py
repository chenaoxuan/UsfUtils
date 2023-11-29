"""
Format various data types.
"""

from typing import Union
from .dict import UsfDict

__all__ = [
    'num_to_str',
    'dict_to_str'
]


def num_to_str(num: float) -> str:
    """
    Automatically convert a positive number to its appropriate unit(thousand million billion) and round it to two
    decimal places.
    :param num: A positive number
    :return: Formatted results
    """
    if num is None:
        raise TypeError('The num cannot be None')
    if num < 0:
        raise TypeError('The num cannot be negative')
    if num < 1000:
        num = round(num, 2)
        if num == 1000:
            return '1.0K'
        return str(num)
    units = ['', 'K', 'M', 'B']
    unit_index = 0
    mul_acc = 1
    copy_num = num
    while copy_num >= 1000 and unit_index < len(units) - 1:
        copy_num /= 1000
        mul_acc *= 1000
        unit_index += 1
    num = int(round(num / int(mul_acc / 1000), -1) / 10)
    if num == 100000 and unit_index + 1 <= len(units) - 1:
        unit_index += 1
        num = 100
    return str(int(num / 100)) + '.' + "{:02d}".format(num % 100) + units[unit_index]


def dict_to_str(opt: Union[UsfDict, dict], indent_level=1) -> str:
    """
    Indent dict according to hierarchical relationships and convert it to str.
    :param opt:
    :param indent_level:
    :return:
    """
    msg = '\n'
    for k, v in opt.items():
        if isinstance(v, UsfDict):
            msg += ' ' * (indent_level * 2) + k + ':['
            msg += dict_to_str(v, indent_level + 1)
            msg += ' ' * (indent_level * 2) + ']\n'
        else:
            msg += ' ' * (indent_level * 2) + k + ': ' + str(v) + '\n'
    return msg
