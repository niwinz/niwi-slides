# -*- coding: utf-8 -*-


from cffi import FFI
ffi = FFI()
ffi.cdef("""
typedef struct Point {
    double x, y;
} Point;

double distance(Point *p1, Point *p2);
""")

c_lib = ffi.dlopen("./libsample.so")

distance = c_lib.distance
p1 = ffi.new("Point *", [1, 2])
p2 = ffi.new("Point *", [4, 5])
