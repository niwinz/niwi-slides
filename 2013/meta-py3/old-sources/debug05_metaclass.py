# -*- coding: utf-8 -*-

from functools import wraps

def debug(func):
    func_name = func.__qualname__

    @wraps(func)
    def _wrapper(*args, **kwargs):
        print(func_name)
        return func(*args, **kwargs)

    return _wrapper


def debugmethods(cls):
    for name, value in vars(cls).items():
        if callable(value):
            setattr(cls, name, debug(value))
    return cls


class debugmeta(type):
    def __new__(clstype, name, bases, attrs):
        cls = super().__new__(clstype, name, bases, attrs)
        return debugmethods(cls)


class Base(object, metaclass=debugmeta):
    pass


class SpamFoo(Base):
    def foo(self):
        pass

    def bar(self):
        pass


class SpamBar(Base):
    def foo(self):
        pass

    def bar(self):
        pass


