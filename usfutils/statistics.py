"""
Some mathematical and statistical functions, such as obtaining model parameters, etc.
"""
import torch

__all__ = [
    'get_format_num',
    'get_params_num'
]


def get_format_num(num: float) -> str:
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
    return str(int(num / 100)) + '.' + str(num % 100) + units[unit_index]


def get_params_num(model: torch.nn.Module, verbose=False) -> int:
    """
    Get the number of parameters in the Pytorch model
    :param model: A pytorch model.
    :param verbose: If true, output the number of parameters.
    :return: An integer that denotes the total number of parameters in the model.
    """
    total_params = sum(p.numel() for p in model.parameters())
    if verbose:
        print(f"{model.__class__.__name__} has {get_format_num(total_params)} params.")
    return total_params
