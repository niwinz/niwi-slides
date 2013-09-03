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


class Descriptor(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class TypedDescriptor(Descriptor):
    _type = None

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError("unexpected type for {0}".format(self.name))
        super().__set__(instance, value)



class Integer(TypedDescriptor):
    _type = int


class Point(Struct):
    _fields = ["x", "y"]

    x = Integer("x")
    y = Integer("y")
