from _ctypes import POINTER
from ctypes import CDLL, c_bool, c_char_p, c_int, c_uint8


def ri_params(lib: CDLL) -> None:
    """Indicate the types of arguments for functions."""
    lib.RI_SDK_InitSDK.argtypes = [c_int, POINTER(c_char_p)]
    lib.RI_SDK_CreateModelComponent.argtypes = [
        c_char_p,
        c_char_p,
        c_char_p,
        POINTER(c_int),
        POINTER(c_char_p),
    ]
    lib.RI_SDK_LinkPWMToController.argtypes = [c_int, c_int, c_uint8, POINTER(c_char_p)]
    lib.RI_SDK_LinkLedToController.argtypes = [
        c_int,
        c_int,
        c_int,
        c_int,
        c_int,
        POINTER(c_char_p),
    ]
    lib.RI_SDK_LinkServodriveToController.argtypes = [
        c_int,
        c_int,
        c_int,
        POINTER(c_char_p),
    ]
    lib.RI_SDK_exec_RGB_LED_SinglePulse.argtypes = [
        c_int,
        c_int,
        c_int,
        c_int,
        c_int,
        c_bool,
        POINTER(c_char_p),
    ]
    lib.RI_SDK_exec_ServoDrive_TurnByPulse.argtypes = [c_int, c_int, POINTER(c_char_p)]
    lib.RI_SDK_DestroyComponent.argtypes = [c_int, POINTER(c_char_p)]
    lib.RI_SDK_exec_RGB_LED_Stop.argtypes = [c_int, POINTER(c_char_p)]
    lib.RI_SDK_sigmod_PWM_ResetAll.argtypes = [c_int, POINTER(c_char_p)]
    lib.RI_SDK_DestroySDK.argtypes = [c_bool, POINTER(c_char_p)]
    lib.RI_SDK_exec_RGB_LED_FlashingWithFrequency.argtypes = [
        c_int,
        c_int,
        c_int,
        c_int,
        c_int,
        c_int,
        c_bool,
        POINTER(c_char_p),
    ]
    lib.RI_SDK_exec_RGB_LED_Flicker.argtypes = [
        c_int,
        c_int,
        c_int,
        c_int,
        c_int,
        c_int,
        c_bool,
        POINTER(c_char_p),
    ]
    lib.RI_SDK_exec_ServoDrive_Turn.argtypes = [
        c_int,
        c_int,
        c_int,
        c_bool,
        POINTER(c_char_p),
    ]
