def set_default_params() -> dict[str, int]:
    return {
        "body_start_pulse": 1500,  # стартовая позиция тела
        "arrowR_start_pulse": 2000,  # стартовая позиция правой стрелы
        "arrowL_start_pulse": 1000,  # стартовая позиция левой стрелы
        "claw_start_pulse": 1000,  # стартовая позиция клешни
        "claw_rotate_start_pulse": 1500,  # стартовая позиция поворота клешни
    }


def set_final_parameters():
    return {
        "arrowR_over_cube_position": -30,  # позиция правой стрелы над кубиком
        "arrowL_over_cube_position": -10,  # позиция левой стрелы над кубиком
        "claw_unclenched_position": 80,  # позиция открытой клешни
        "arrowR_cube_position": -75,   # позиция правой стрелы на месте кубика
        "arrowL_cube_position": 55,  # позиция левой стрелы на месте кубика
    }


def set_speed():
    return {"speed": 120}  # скорость в градусах в секунду


def set_login_level():
    return {"login_level": 2}  # уровень логирования


