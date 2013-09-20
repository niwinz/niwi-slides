# -*- coding: utf-8 -*-

import pickle

class A(object):
    def __new__(cls, *args, **kwargs):
        print("A.__new__", cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("A.__init__", self, args, kwargs)
        self.args = args
        self.kwargs = kwargs
