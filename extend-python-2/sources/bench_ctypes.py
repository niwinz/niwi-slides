# -*- coding: utf-8 -*-

import ctypes

c_lib = ctypes.CDLL("./libsample.so")

gcd = c_lib.gcd
gcd.argtypes = [ctypes.c_int, ctypes.c_int]
gcd.restype = ctypes.c_int
