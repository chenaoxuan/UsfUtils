from usfutils.load import instantiate_from_config
from usfutils.config import load_yaml
from usfutils.statistics import get_params_name

if __name__ == '__main__':
    config = load_yaml("C:\\Users\\A\Desktop\\train_subj_sdu.yaml")
    model = instantiate_from_config(config.model)
    print(get_params_name(model, level=2))
