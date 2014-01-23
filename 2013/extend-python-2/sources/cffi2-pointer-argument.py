# -*- coding: utf-8 -*-

from cffi import FFI
ffi = FFI()
ffi.cdef("int divide(int, int, int*);")

c_lib = ffi.dlopen("./libsample.so")
_divide = c_lib.divide

def divide(x:int, y:int) -> int:
    rest = ffi.new("int *")
    result = _divide(x, y, rest)
    return result, rest[0]
