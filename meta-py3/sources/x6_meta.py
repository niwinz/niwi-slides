# -*- coding: utf-8 -*-

from inspect import Signature, Parameter
import collections

class Descriptor(object):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class MetaStruct(type):
    def __prepare__(cls, *args, **kwargs):
        return collections.OrderedDict()

    def __new__(clst, name, bases, attrs):
        params = []
        param_type = Parameter.POSITIONAL_OR_KEYWORD

        for name, attr in attrs.items():
            if isinstance(attr, Descriptor):
                params.append(Parameter(name, param_type))
                attr.name = name

        attrs = dict(attrs)
        attrs["__signature__"] = Signature(params)

        return super().__new__(clst, name, bases, attrs)


class Struct(object, metaclass=MetaStruct):
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class TypedDescriptor(Descriptor):
    _type = None

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError("unexpected type for {0}".format(self.name))
        super().__set__(instance, value)


class Integer(TypedDescriptor):
    _type = int


class Point(Struct):
    x = Integer()
    y = Integer()
