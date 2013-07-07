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

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("int expected")
        if value < 0:
            raise ValueError("value must be > 0")
        self._age = value
