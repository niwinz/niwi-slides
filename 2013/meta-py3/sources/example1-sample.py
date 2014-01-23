# -*- coding: utf-8 -*-

class Spam(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello {0}".format(self.name))
