# -*- coding: utf-8 -*-

class Struct(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name, value in kwargs.items():
            setattr(self, name, value)


class Person(Struct):
    _fields = ['name', 'age']
