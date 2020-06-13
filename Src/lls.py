import sys
import os


def get_config():
    ENV_CONFIG='LLC_CONFIG'

    dir_script = os.path.dirname(os.path.realpath(__file__))
    default_config = dir_script + '/config.py'

    if ENV_CONFIG in os.environ:
        fconfig = os.environ[ENV_CONFIG]
    else:
        fconfig = default_config

    with open(fconfig) as fd:
        sconfig = fd.read()

        glbl = {}
        lcl = {}
        exec(sconfig, glbl, lcl)
        return lcl
