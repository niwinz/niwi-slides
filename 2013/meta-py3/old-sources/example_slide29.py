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


@debugmethods
class Spam(object):
    def foo(self):
        pass

    def bar(self):
        pass

    def dokk(self):
        pass
