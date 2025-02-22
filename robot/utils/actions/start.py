from ctypes import CDLL

from robot.utils.actions.default_position import start_position_all_servo
from robot.utils.actions.get import get
from robot.utils.actions.put import put
from robot.utils.actions.rotate import rotate_body
from robot.utils.destruct import destruct_all
from robot.utils.init_device import init_device


def start(
    lib: CDLL,
    default_params: dict,
    device: dict,
    descriptors_params: list[dict],
):
    """Функция для запуска программы."""
    # Инициализируем библиотеку и компоненты
    errCode, errText = init_device(
        lib=lib,
        default_params=default_params,
        device=device,
    )
    if errCode != 0:
        return errCode, errText

    # Приводим сервоприводы к стартовой позиции
    errCode, errText = start_position_all_servo(
        lib=lib,
        device=device,
        descriptors_params=descriptors_params,
    )
    if errCode != 0:
        return errCode, errText

    # Двигаем тело к местонахождению кубика
    errCode, errText = rotate_body(
        45,
        default_params.get("speed"),
    )
    if errCode != 0:
        return errCode, errText

    # Берем кубик
    errCode, errText = get(
        lib=lib,
        default_params=default_params,
        device=device,
    )
    if errCode != 0:
        return errCode, errText

    # Двигаем тело к новому местонахождению кубика
    errCode, errText = rotate_body(
        -90,
        default_params.get("speed"),
    )
    if errCode != 0:
        return errCode, errText

    # Кладем кубик
    errCode, errText = put(
        lib=lib,
        default_params=default_params,
        device=device,
    )
    if errCode != 0:
        return errCode, errText

    # Возвращаем тело в стартовое положение
    errCode, errText = rotate_body(
        45,
        default_params.get("speed"),
    )
    if errCode != 0:
        return errCode, errText

    # Уничтожаем компоненты и библиотеку
    errCode, errText = destruct_all(
        lib=lib,
        device=device,
    )
    if errCode != 0:
        return errCode, errText
    return errCode, errText
