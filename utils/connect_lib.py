from ctypes import cdll, CDLL


def connect_lib() -> CDLL:
    path_lib = r"E:\RoboIntellect\ri_sdk\ri_sdk_x64\librisdk.dll"
    return cdll.LoadLibrary(path_lib)