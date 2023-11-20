from usfutils.config import UsfConfig
from usfutils.logger import get_root_logger


def f(**kwargs):
    for key, value in kwargs.items():
        print(key, value, type(value))


if __name__ == '__main__':
    logger = get_root_logger(log_path='t')
    a = UsfConfig.load(path="t/t/1.yaml")
    UsfConfig.copy_opt_file(file_path="t/t/1.yaml", experiments_path='t')
    logger.info(UsfConfig.dict_to_str(a))
