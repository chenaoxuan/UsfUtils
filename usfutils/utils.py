"""
Other more basic operations.
"""

import random
import logging
from typing import Optional
from .time import get_time_int

__all__ = [
    'set_seed_everything',
]


def set_seed_everything(seed: Optional[int] = None, deterministic: bool = False,
                        logger: Optional[logging.Logger] = None) -> None:
    """
    Set seed for pseudo-random number generators in: pytorch, numpy, python.random.
    NOTES:Before Python version 1.9, after setting the seed, different Dataloaders' wokers would load the same data.
    Upgrade the Python version or use the following code:
    '''
        def worker_init_fn(worker_id):
            np.random.seed(np.random.get_state()[1][0] + worker_id)
        dataloader = DataLoader(dataset, batch_size=2, num_workers=2, worker_init_fn=worker_init_fn)
    '''
    :param logger: Logger
    :param seed: The integer value seed for global random state. If `None`, will select it randomly.
    :param deterministic: Some other operations of pytorch will also have strict determinacy, but this option may reduce training speed.
    :return: None
    """
    if logger is None:
        logger = logging.getLogger('set_seed_everything')
        format_str = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(format_str)
        logger.addHandler(stream_handler)
        logger.setLevel(logging.INFO)
    try:
        import numpy as np
        max_value = np.iinfo(np.uint32).max
        min_value = np.iinfo(np.uint32).min
        if seed is None:
            seed = random.randint(min_value, max_value)
        elif not (min_value <= seed <= max_value):
            logger.warning(f"{seed} is not in bounds, Numpy accepts from {min_value} to {max_value}")
            seed = random.randint(min_value, max_value)
        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch
        max_value = 0xffff_ffff_ffff_ffff
        min_value = -0x8000_0000_0000_0000
        if seed is None:
            seed = random.randint(min_value, max_value)
        elif not (min_value <= seed <= max_value):
            logger.warning(f"{seed} is not in bounds, Pytorch accepts from {min_value} to {max_value}")
            seed = random.randint(min_value, max_value)
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
            if deterministic:
                torch.use_deterministic_algorithms(True)
            logger.info('Pytorch enables the use of deterministic algorithms, which may affect training speed.')
    except:
        pass
    if seed is None:
        seed = get_time_int()
    random.seed(seed)
    logger.info(f"Global seed set to {seed}")
