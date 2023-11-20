from usfutils.statistics import get_params_num
from usfutils.utils import get_obj_from_str

if __name__ == '__main__':
    net = get_obj_from_str('usfutils.net.Net')(in_features=10, out_features=20)
    _ = get_params_num(net, verbose=True)

