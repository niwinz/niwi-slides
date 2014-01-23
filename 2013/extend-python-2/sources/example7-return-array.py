# -*- coding: utf-8 -*-

import ctypes
c_lib = ctypes.CDLL("./libsample.so")
libc = ctypes.CDLL(None)

cb_type = ctypes.CFUNCTYPE(None, ctypes.c_int)

_range = c_lib.range
_range.argtypes = (ctypes.c_int, ctypes.c_int)
_range.restype = ctypes.c_void_p

def crange(length:int, start:int=0) -> list:
    ptr = _range(length, start)
    ptr_type = ctypes.POINTER(ctypes.c_int*length)
    result = ctypes.cast(ptr, ptr_type)

    try:
        return [i for i in result.contents]
    finally:
        libc.free(ptr)

#print(crange(5, 5))
