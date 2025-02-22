from ctypes import c_int


def init_descriptors() -> dict:
    """Инициализация дескрипторов."""
    return {
        "i2c": c_int(),  # дескриптор i2c
        "pwm": c_int(),  # дескриптор pwm
        "body": c_int(),  # дескриптор сервопривода тела
        "claw": c_int(),  # дескриптор сервопривода клешни
        "arrowR": c_int(),  # дескриптор сервопривода правой стрелы
        "arrowL": c_int(),  # дескриптор сервопривода левой стрелы
        "clawRotate": c_int(),  # дескриптор сервопривода поворота клешни
        "led": c_int(),  # дескриптор светодиода
    }


def set_up_descriptor(default_params: dict[str:int], device: dict) -> list[dict]:
    """Установка дескрипторов."""
    return [
        {
            "descriptor": device["body"],
            "start_position": default_params.get("body_start_pulse"),
        },
        {
            "descriptor": device["claw"],
            "start_position": default_params.get("claw_start_pulse"),
        },
        {
            "descriptor": device["arrowR"],
            "start_position": default_params.get("arrowR_start_pulse"),
        },
        {
            "descriptor": device["arrowL"],
            "start_position": default_params.get("arrowL_start_pulse"),
        },
        {
            "descriptor": device["clawRotate"],
            "start_position": default_params.get("claw_rotate_start_pulse"),
        },
    ]
