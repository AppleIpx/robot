# destructServos - уничтожает сервоприводы
from ctypes import CDLL, c_bool, c_char_p, c_int


def destruct_servos(lib: CDLL, descriptors_params: dict):
    """Уничтожаем сервопривод."""
    err_text_c = c_char_p()
    err_code = c_int

    for i in range(len(descriptors_params)):
        if (
            err_code := lib.RI_SDK_DestroyComponent(
                descriptors_params[i]["descriptor"],
                err_text_c,
            )
            != 0
        ):
            return err_code, err_text_c

    return err_code, err_text_c


# destruct - уничтожает все компоненты и библиотеку
def destruct_all(device: dict, lib: CDLL):
    """
    Выполняем одиночное свечение светодиодом.

    Передаем дескриптор светодиода,3 параметра цвета(RGB),
    и включаем асинхронный режим работы.
    """
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
    err_code, err_text_c = destruct_servos(lib=lib, descriptors_params=device)
    if err_code != 0:
        return err_code, err_text_c
    # останавливаем свечение светодиода с определенным дескриптором
    if err_code := lib.RI_SDK_exec_RGB_LED_Stop(device["led"], err_text_c) != 0:
        return err_code, err_text_c
    # удаляем компонент светодиода по дескриптору
    if err_code := lib.RI_SDK_DestroyComponent(device["led"], err_text_c) != 0:
        return err_code, err_text_c
    # сбрасываем все порты на ШИМ
    if err_code := lib.RI_SDK_sigmod_PWM_ResetAll(device["pwm"], err_text_c) != 0:
        return err_code, err_text_c
    # удаляем компонент ШИМ
    if err_code := lib.RI_SDK_DestroyComponent(device["pwm"], err_text_c) != 0:
        return err_code, err_text_c
    # удаляем компонент i2c
    if err_code := lib.RI_SDK_DestroyComponent(device["i2c"], err_text_c) != 0:
        return err_code, err_text_c
    # удаляем sdk со всеми компонентами в реестре компонентов
    if err_code := lib.RI_SDK_DestroySDK(c_bool(True), err_text_c) != 0:
        return err_code, err_text_c

    return err_code, err_text_c
