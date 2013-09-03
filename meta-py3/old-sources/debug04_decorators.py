# -*- coding: utf-8 -*-

from functools import wraps, partial

def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    func_name = func.__qualname__
    @wraps(func)
    def _wrapper(*args, **kwargs):
        print(prefix, func_name)
        return func(*args, **kwargs)

    return _wrapper


@debug(prefix="****")
def add(x, y):
    return x + y
