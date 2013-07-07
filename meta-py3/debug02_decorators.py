# -*- coding: utf-8 -*-

from functools import wraps

def debug(func):
    func_name = func.__qualname__

    @wraps(func)
    def _wrapper(*args, **kwargs):
        print(func_name)
        return func(*args, **kwargs)

    return _wrapper


@debug
def add(x, y):
    return x + y

@debug
def sub(x, y):
    return x - y

@debug
def mul(x, y):
    return x * y

@debug
def div(x, y):
    return x / y
