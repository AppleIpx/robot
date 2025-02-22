from ctypes import CDLL, c_bool, c_char_p


def get(lib: CDLL, device: dict, default_params: dict):
    """Функция хватания."""
    err_text_c = c_char_p()
    # выполняем мерцание светодиодом, передаем дескриптор светодиода,
    # 3 параметра цвета(RGB), продолжительность, кол-во повторений
    # и включаем асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_RGB_LED_FlashingWithFrequency(
            device["led"],
            0,
            0,
            255,
            500,
            0,
            c_bool(True),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор стрелы,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["arrowR"],
            default_params.get("arrowR_over_cube_position"),
            default_params.get("speed"),
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор стрелы,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["arrowL"],
            default_params.get("arrowR_over_cube_position"),
            default_params.get("speed"),
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
            device["claw"],
            default_params.get("arrowR_over_cube_position"),
            default_params.get("speed"),
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор стрелы,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["arrowR"],
            (
                default_params.get("arrowR_cube_position")
                - default_params.get("arrowR_over_cube_position")
            ),
            default_params.get("speed"),
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор стрелы,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["arrowL"],
            (
                default_params.get("arrowL_cube_position")
                - default_params.get("arrowL_over_cube_position")
            ),
            default_params.get("speed"),
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
            device["claw"],
            (-1) * default_params.get("claw_unclenched_position"),
            default_params.get("speed"),
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор стрелы,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["arrowR"],
            (-1) * default_params.get("arrowR_cube_position"),
            default_params.get("speed"),
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # выполняем поворот на заданный угол, передаем дескриптор стрелы,
    # угол, скорость и асинхронный режим работы
    if (
        err_code := lib.RI_SDK_exec_ServoDrive_Turn(
            device["arrowL"],
            (-1) * default_params.get("arrowL_cube_position"),
            default_params.get("speed"),
            c_bool(False),
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c

    return err_code, err_text_c
