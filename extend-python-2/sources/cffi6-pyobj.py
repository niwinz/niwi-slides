# -*- coding: utf-8 -*-

# TODO: this does not works.

from cffi import FFI
ffi = FFI()
ffi.cdef("""
    void print_address(void *obj);
""")

c_lib = ffi.dlopen("./libsample2.so")


class Foo(object):
    def __init__(self, address):
        self.address = address

    def get_address(self):
        return self.address

print_address = c_lib.print_address

instance = Foo("Foo Bar")
_instance = ffi.new_handle(instance)

print_address(instance)
