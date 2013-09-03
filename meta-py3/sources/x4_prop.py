# -*- coding: utf-8 -*-

from inspect import Signature, Parameter


class Struct(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        params = [Parameter(field, Parameter.POSITIONAL_OR_KEYWORD)
                  for field in self._fields]
        sig = Signature(params)
        bound_values = sig.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Point(Struct):
    _fields = ["x", "y"]

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("unexpected type for x")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("unexpected type for x")
        self._y = value
