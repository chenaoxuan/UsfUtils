"""
Some mathematical and statistical functions, such as obtaining model parameters, etc.
"""
import torch
from .format import num_to_str, dict_to_str

__all__ = [
    'get_params_num',
    'get_params_name'
]


def get_params_num(model: torch.nn.Module, verbose: bool = False) -> int:
    """
    Get the number of parameters in the Pytorch model
    :param model: A pytorch model.
    :param verbose: If true, output the number of parameters.
    :return: An integer that denotes the total number of parameters in the model.
    """
    total_params = sum(p.numel() for p in model.parameters())
    if verbose:
        print(f"{model.__class__.__name__} has {num_to_str(total_params)} params.")
    return total_params


def get_params_name(model: torch.nn.Module, level: int = 1) -> list:
    """
    Identify which modules in the model have parameters.
    :param model: Pytorch model.
    :param level: The hierarchy of module names.
    :return: A list that denotes the names of modules with parameters.
    """
    if model is None:
        raise TypeError('The model cannot be None')
    named_params_list = []
    for name, param in model.named_parameters():
        parts = name.split(".")
        pre_name = ".".join(parts[:level])
        if pre_name not in named_params_list:
            named_params_list.append(pre_name)
    return named_params_list
