# -*- coding: utf-8 -*-

import ctypes
c_lib = ctypes.CDLL("./libsample2.so")


class Foo(object):
    def __init__(self, address):
        self.address = address

    def get_address(self):
        return self.address


prototype = ctypes.PYFUNCTYPE(None, ctypes.py_object)
print_address = prototype(('print_address', c_lib))

#instance = Foo("Foo Bar")
#print_address(instance)
