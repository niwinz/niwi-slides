# -*- coding: utf-8 -*-

from functools import wraps

def nothing_with_wraps(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return _wrapper

def nothing_without_wraps(func):
    def _wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return _wrapper

@nothing_with_wraps
def foo():
    pass

@nothing_without_wraps
def bar():
    pass

