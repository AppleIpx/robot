from ctypes import CDLL, c_bool, c_char_p


# rotateBody - вращение тела в указанный угол
def rotate_body(angle: int, speed: int, lib: CDLL, device: dict):
    """Вращение тела в указанный угол."""
    err_text_c = c_char_p()
    # выполняем мигание с заданной частотой, передаем дескриптор светодиода,
    # 3 параметра цвета(RGB), частоту, продолжительность и включаем асинхронный режим.
    if (
        err_code := lib.RI_SDK_exec_RGB_LED_FlashingWithFrequency(
            device["led"],
            0,
            255,
            0,
            5,
            0,
            c_bool(True),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор тела,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["body"],
            angle,
            speed,
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор клешни,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["clawRotate"],
            45,
            speed,
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор клешни,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["clawRotate"],
            -45,
            speed,
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c

    return err_code, err_text_c
