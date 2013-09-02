# -*- coding: utf-8 -*-

import ctypes
c_lib = ctypes.CDLL("./libsample.so")


cb_type = ctypes.CFUNCTYPE(None, ctypes.c_int)

_sum_with_cb = c_lib.sum_with_cb
_sum_with_cb.argtypes = (ctypes.c_int, ctypes.c_int, cb_type)
_sum_with_cb.restype = None

def sum(x:int, y:int, callback) -> None:
    cb = cb_type(callback)
    _sum_with_cb(x, y, cb)

def sample_cb(result:int) -> None:
    print("Result:", result)

#sum(1, 2, sample_cb)
