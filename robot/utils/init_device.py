from ctypes import CDLL, c_char_p, c_uint8

from robot.example import initServos


def init_device(lib: CDLL, default_params: dict, device: dict):
    """Инициализация девайса."""
    err_text_c = c_char_p()
    # Вызываем функцию инициализации
    if err_code := lib.RI_SDK_InitSDK(default_params.get("logLevel"), err_text_c) != 0:
        return err_code, err_text_c
    # создаем компонент ШИМ с конкретной моделью как исполняемое устройство,получаем дескриптор сервопривода
    if (
        err_code := lib.RI_SDK_CreateModelComponent(
            "connector".encode(),
            "pwm".encode(),
            "pca9685".encode(),
            device["pwm"],
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c

    # создаем компонент i2c адаптера
    # Здесь осуществлен примитивное определение подключенной модели адаптера
    # Сначала пробуем создать i2c адаптер модели ch341 и связать с ним ШИМ
    if (
        err_code := lib.RI_SDK_CreateModelComponent(
            "connector".encode(),
            "i2c_adapter".encode(),
            "ch341".encode(),
            device["i2c"],
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c

    # связываем i2c адаптер с ШИМ по адресу 0x40
    if (
        lib.RI_SDK_LinkPWMToController(
            device["pwm"],
            device["i2c"],
            c_uint8(0x40),
            err_text_c,
        )
        != 0
    ):
        # Если не получается то пробуем создать i2c адаптер модели cp2112
        if (
            err_code := lib.RI_SDK_CreateModelComponent(
                "connector".encode(),
                "i2c_adapter".encode(),
                "cp2112".encode(),
                device["i2c"],
                err_text_c,
            )
            != 0
        ):
            return err_code, err_text_c
        # связываем i2c адаптер с ШИМ по адресу 0x40
        if (
            err_code := lib.RI_SDK_LinkPWMToController(
                device["pwm"],
                device["i2c"],
                c_uint8(0x40),
                err_text_c,
            )
            != 0
        ):
            return err_code, err_text_c

    # создаем компонент светодиода с конкретной моделью (ky016) как исполняемое устройство и получаем дескриптор светодиода
    if (
        err_code := lib.RI_SDK_CreateModelComponent(
            "executor".encode(),
            "led".encode(),
            "ky016".encode(),
            device["led"],
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # связываем светодиод с ШИМ,передаем значения трех пинов к которым подключен светодиод
    if (
        err_code := lib.RI_SDK_LinkLedToController(
            device["led"],
            device["pwm"],
            15,
            14,
            13,
            err_text_c,
        )
        != 0
    ):
        return err_code, err_text_c
    # инициализируем сервоприводы
    err_code, err_text_c = initServos()
    if err_code != 0:
        return err_code, err_text_c
    return err_code, err_text_c.value
