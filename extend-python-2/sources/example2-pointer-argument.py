# -*- coding: utf-8 -*-

import ctypes

c_lib = ctypes.CDLL("./libsample.so")

_divide = c_lib.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int,
                    ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int


def divide(x:int, y:int) -> int:
    rest = ctypes.c_int()
    result = _divide(x, y, rest)
    return result, rest.value
