# -*- coding: utf-8 -*-

from inspect import Signature, Parameter

class Struct(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        params = [Parameter(field, Parameter.POSITIONAL_OR_KEYWORD)
                  for field in self._fields]
        sig = Signature(params)
        bound_values = sig.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)



class Point(Struct):
    _fields = ["x", "y"]
