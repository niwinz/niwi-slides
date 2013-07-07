# -*- coding: utf-8 -*-

from functools import wraps

def debug(prefix=''):
    def _decorator(func):
        func_name = func.__qualname__
        @wraps(func)
        def _wrapper(*args, **kwargs):
            print(prefix, func_name)
            return func(*args, **kwargs)

        return _wrapper
    return _decorator

@debug(prefix="****")
def add(x, y):
    return x + y
