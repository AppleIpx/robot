from utils.connect_lib import connect_lib
from utils.descriptors import init_descriptors, set_up_descriptor
from utils.init_ri_params import ri_params
from utils.set_up_params import (
    set_default_params,
    set_final_parameters,
    set_login_level,
    set_speed,
)

from robot.utils.actions.start import start


def get_default_params() -> dict[str, int]:
    """Function that get default params."""
    return (
        set_default_params() | set_final_parameters() | set_speed() | set_login_level()
    )


def collect_data():
    lib = connect_lib()
    default_params = get_default_params()
    device = init_descriptors()
    descriptors_params = set_up_descriptor(default_params=default_params, device=device)
    ri_params(lib=lib)
    return lib, default_params, descriptors_params, device


# Главная функция запускающая все остальное
def main():
    lib, default_params, descriptors_params, device = collect_data()
    errCode, errText = start(
        lib=lib,
        default_params=default_params,
        descriptors_params=descriptors_params,
        device=device,
    )
    if errCode != 0:
        print(errCode, errText)
        return

    print("Success", device)
