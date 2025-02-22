import time
from ctypes import CDLL, c_bool, c_char_p


def start_position(descriptors_params: dict, lib: CDLL):
    """
    Установка начального положения.

    Выполняется поворот сервопривода в заданный угол,
    передаем дескриптор сервопривода, значение угла.
    """
    err_text_c = c_char_p()
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_TurnByPulse(
            descriptors_params["descriptor"],
            descriptors_params["start_position"],
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c

    time.sleep(0.5)

    return err_code, err_text_c


def start_position_all_servo(lib: CDLL, device: dict, descriptors_params: list[dict]):
    """Функция возвращения всех сервоприводов в начальное состояние."""
    err_text_c = c_char_p()
    if (
        err_code := lib.RI_SDK_exec_RGB_LED_SinglePulse(
            device["led"],
            255,
            0,
            0,
            0,
            c_bool(True),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # приводим сервоприводы в стартовое положение
    for i in range(len(descriptors_params)):
        err_code, err_text_c = start_position(
            descriptors_params=descriptors_params[i],
            lib=lib,
        )
        if err_code != 0:
            return err_code, err_text_c
    if (
        err_code := lib.RI_SDK_exec_RGB_LED_SinglePulse(
            device["led"],
            0,
            255,
            0,
            0,
            c_bool(True),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c

    time.sleep(0.5)

    return err_code, err_text_c.value
