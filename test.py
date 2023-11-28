import argparse
from usfutils.config import UsfConfig

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument(
        '-o',
        '--output',
        type=str,
        default='a.txt',
        help='输出文件名'
    )
    parse.add_argument(
        '-c',
        '--channel',
        type=int,
        default=1,
        help='通道数'
    )
    parse.add_argument(
        '-f',
        '--flag',
        action='store_true',
        help='通道数'
    )
    arg = parse.parse_args()

    config = UsfConfig.load("C:\\Users\\cax11\\Desktop\\train_subj_sdu.yaml")
    config.update(arg)
    config.update({"output": (1, 2, 3), "flag": 1})

    UsfConfig.to_yaml(config,"C:\\Users\\cax11\\Desktop\\1.yaml")
    print(UsfConfig.dict_to_str(config))