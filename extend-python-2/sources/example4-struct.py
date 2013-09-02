# -*- coding: utf-8 -*-

import ctypes
c_lib = ctypes.CDLL("./libsample.so")

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]

distance = c_lib.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double

p1 = Point(1, 2)
p2 = Point(4, 5)
