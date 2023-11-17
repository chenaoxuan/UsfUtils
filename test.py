import os
from usfutils.logger import get_env_info, get_root_logger
from usfutils.dist import get_dist_info

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(current_directory)
    logger = get_root_logger(log_path=current_directory)
    logger.info("Hello")
