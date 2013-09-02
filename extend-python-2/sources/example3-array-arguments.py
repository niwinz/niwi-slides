# -*- coding: utf-8 -*-

import ctypes

c_lib = ctypes.CDLL("./libsample.so")

class DoubleArrayType(object):
    @classmethod
    def from_param(cls, param):
        type_cls = (ctypes.c_double) * len(param)
        return type_cls(*param)

_avg = c_lib.avg
_avg.argtypes = (DoubleArrayType, ctypes.c_int)
_avg.restype = ctypes.c_double

def avg(values:list) -> float:
    return _avg(values, len(values))
