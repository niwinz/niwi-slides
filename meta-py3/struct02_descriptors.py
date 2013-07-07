# -*- coding: utf-8 -*-


class Descriptor(object):
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        print("__get__")
        if instance is None:
            return self
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        print("__set__ -> {0}".format(value))
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        print("__delete__")
        del instance.__dict__[self.name]


class Spam(object):
    foo = Descriptor("foo")
