# -*- coding: utf-8 -*-

class Point(object):
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
