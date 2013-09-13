# -*- coding: utf-8 -*-

from cffi import FFI
ffi = FFI()
ffi.cdef("double avg(double*, int);")

c_lib = ffi.dlopen("./libsample.so")

def avg(values:list) -> float:
    values_ptr = ffi.new("double[]", values)
    result = c_lib.avg(values_ptr, len(values))
    return result

#print("Result:", avg([1,2,3]))
