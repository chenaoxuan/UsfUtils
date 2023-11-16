import basicsr
import omegaconf

from caxutils.utils import get_time_str
from caxutils.dir import scandir

if __name__ == '__main__':
    for item in scandir("C:\\Users\\A\\Desktop", suffix=('.png','.md')):
        print(item)
