from ctypes import CDLL, c_char_p, c_int


def init_servos(lib: CDLL, servos: dict, device):
    errTextC = c_char_p()
    errCode = c_int
    # создаем 5 сервоприводов и линкуем их к пинам 0-4
    for i in range(len(servos)):
        # создаем компонент сервопривода с конкретной моделью как исполняемое устройство и получаем дескриптор сервопривода
        errCode = lib.RI_SDK_CreateModelComponent(
            "executor".encode(),
            "servodrive".encode(),
            "mg90s".encode(),
            servos[i]["descriptor"],
            errTextC,
        )
        if errCode != 0:
            return errCode, errTextC
        # связываем сервопривод с ШИМ,передаем дескриптор сервопривода и ШИМ
        errCode = lib.RI_SDK_LinkServodriveToController(
            servos[i]["descriptor"], device["pwm"], i, errTextC,
        )
        if errCode != 0:
            return errCode, errTextC
    return errCode, errTextC
