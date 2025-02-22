from ctypes import CDLL, c_char_p, c_int


def init_servos(lib: CDLL, servos: dict, device: dict) -> tuple:
    """
    Cоздаем 5 сервоприводов и линкуем их к пинам 0-4.

    Cоздаем компонент сервопривода с конкретной моделью как исполняемое устройство
    и получаем дескриптор сервопривода.
    Затем связываем сервопривод с ШИМ, передаем дескриптор сервопривода и ШИМ.
    """
    err_text_c = c_char_p()
    err_code = c_int()
    for i in range(len(servos)):
        if (
            err_code := lib.RI_SDK_CreateModelComponent(
                "executor".encode(),
                "servodrive".encode(),
                "mg90s".encode(),
                servos[i]["descriptor"],
                err_text_c,
            )
            != 0
        ):
            return err_code, err_text_c
        if (
            err_code := lib.RI_SDK_LinkServodriveToController(
                servos[i]["descriptor"],
                device["pwm"],
                i,
                err_text_c,
            )
            != 0
        ):
            return err_code, err_text_c
    return err_code, err_text_c
