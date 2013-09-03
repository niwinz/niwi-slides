# -*- coding: utf-8 -*-


from inspect import Signature, Parameter

class Point(object):
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise TypeError("unexpected type for x")
        if not isinstance(y, int):
            raise TypeError("unexpected type for x")

        self.y = y
        self.x = x

