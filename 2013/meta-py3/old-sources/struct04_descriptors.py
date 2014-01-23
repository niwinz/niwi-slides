# -*- coding: utf-8 -*-


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



class TypedDescriptor(Descriptor):
    _type = object

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError("Expected {0}".format(self._type))
        super().__set__(instance, value)


class String(TypedDescriptor):
    _type = str


class Integer(TypedDescriptor):
    _type = int


class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super().__set__(instance, value)


class PositiveInteger(Integer, Positive):
    pass


from collections import OrderedDict

class StructMeta(type):
    @classmethod
    def __prepare__(cls, *args, **kwargs):
        return OrderedDict()

    def __new__(clst, name, bases, attrs):
        fields = [k for k,v in attrs.items()
                    if isinstance(v, Descriptor)]

        for name in fields:
            attrs[name].name = name

        cls = super().__new__(clst, name, bases, attrs)
        cls._fields = fields
        return cls


class Struct(object, metaclass=StructMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name, value in kwargs.items():
            setattr(self, name, value)


class Person(Struct):
    name = String()
    age = PositiveInteger()
