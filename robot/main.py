from utils.connect_lib import connect_lib
from utils.descriptors import set_up_descriptor
from utils.init_ri_params import ri_params
from utils.set_up_params import (
    set_default_params,
    set_final_parameters,
    set_login_level,
    set_speed,
)


def get_default_params():
    return (
        set_default_params() | set_final_parameters() | set_speed() | set_login_level()
    )


def main():
    lib = connect_lib()
    default_params = get_default_params()
    descriptors_params = set_up_descriptor(default_params=default_params)
    ri_params(lib=lib)
