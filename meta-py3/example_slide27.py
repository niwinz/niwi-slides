# -*- coding: utf-8 -*-

from functools import wraps

def debug(func):
    func_name = func.__qualname__

    @wraps(func)
    def _wrapper(*args, **kwargs):
        print(func_name)
        return func(*args, **kwargs)

    return _wrapper


class Spam(object):
    @debug
    def foo(self):
        pass

    @debug
    def bar(self):
        pass

    @debug
    def dokk(self):
        pass


