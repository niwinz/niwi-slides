# -*- coding: utf-8 -*-

from cffi import FFI
ffi = FFI()
ffi.cdef("int gcd(int, int);")

c_lib = ffi.dlopen("./libsample.so")
gcd = c_lib.gcd
