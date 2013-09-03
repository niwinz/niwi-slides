# -*- coding: utf-8 -*-


from cffi import FFI
ffi = FFI()
ffi.cdef("void sum_with_cb(int x, int y, void (*callback)(int));")
c_lib = ffi.dlopen("./libsample.so")

def sample_cb(result:int) -> None:
    print("Result:", result)

def sum(x:int, y:int, callback) -> None:
    cb = ffi.callback("void(int)", sample_cb)
    c_lib.sum_with_cb(x, y, cb)

#sum(1, 2, sample_cb)
