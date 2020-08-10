# code imports
from json import load
from os import getenv
from pathlib import Path
from os.path import dirname


# functions
def get_configs() -> dict:
    '''function to load the configs used by the endpoints

    returns
    -------
    configs : dict
        a dictionary containing the value of all required secrets in the function app
    '''
    env = getenv('FUNCTIONS_ENV')
    current = Path(dirname(__file__)).absolute()
    if env == 'local':
        with open(current.joinpath('local.configs.json'), 'r') as json_file:
            configs = load(json_file)
    else:
        with open(current.joinpath('configs.json'), 'r') as json_file:
            configs = load(json_file)
    return configs