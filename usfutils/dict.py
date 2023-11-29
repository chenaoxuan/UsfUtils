"""
The basic data type in usfutils: UsfDict, inherited from dict.
"""
from typing import Union
import argparse

__all__ = [
    'UsfDict'
]


class UsfDict(dict):
    def __init__(self, d: dict = None, **kwards):
        super().__init__()
        if d is None:
            d = {}
        else:
            d.update(**kwards)
        for k, v in d.items():
            setattr(self, k, v)
        # Class attributes
        for k in self.__class__.__dict__.keys():
            if not (k.startswith('__') and k.endswith('__')) and not k in ('update', 'pop'):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if isinstance(value, (list, tuple)):
            value = [self.__class__(x)
                     if isinstance(x, dict) else x for x in value]
        elif isinstance(value, dict) and not isinstance(value, UsfDict):
            value = UsfDict(value)
        super(UsfDict, self).__setitem__(name, value)

    __setitem__ = __setattr__

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def update(self, e: Union['UsfDict', dict, argparse.Namespace] = None, verbose=True, **kwargs):
        d = e or dict()
        if isinstance(d, argparse.Namespace):
            d = vars(d)
        d.update(kwargs)
        output_msg = []
        for k in d:
            v = self.get(k, None)
            if v is not None and (not isinstance(type(v), type(d[k])) or v != d[k]):
                output_msg.append(str(k))
            setattr(self, k, d[k])
        if verbose and len(output_msg):
            print(f"{output_msg} in UsfDict has been modified!")

    def pop(self, k, d=None):
        delattr(self, k)
        return super(UsfDict, self).pop(k, d)
