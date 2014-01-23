# -*- coding: utf-8 -*-


from cffi import FFI
ffi = FFI()
ffi.cdef("""
    int* range(int length, int start);
    void free(void *);
""")

c_lib = ffi.dlopen("./libsample.so")
libc = ffi.dlopen(None)

def crange(length:int, start:int=0) -> list:
    ptr = c_lib.range(length, start)

    try:
        result = []
        for i in range(length):
            result.append(ptr[i])

        return result
    finally:
        libc.free(ptr)

#print(crange(5, 5))
