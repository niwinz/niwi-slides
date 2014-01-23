# -*- coding: utf-8 -*-


class SomeMeta(type):
    def __new__(clst, name, bases, attrs):
        print("SomeMeta.__new__", clst, name, bases, {})
        return super().__new__(clst, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print("SomeMeta.__init__", cls, name, bases, {})
        super().__init__(name, bases, attrs)


    def __call__(cls, *args, **kwargs):
        print("SomeMeta.__call__", cls, args, kwargs)
        return super().__call__(*args, **kwargs)


class A(metaclass=SomeMeta):
    def __new__(cls, *args, **kwargs):
        print("A.__new__", cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("A.__init__", self, args, kwargs)
        self.args = args
        self.kwargs = kwargs


a = A(2)
