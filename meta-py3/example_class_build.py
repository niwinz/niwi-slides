# -*- coding: utf-8 -*-

# Consider this class

class Spam(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello {0}".format(self.name))


# Process

# Step 1
clsattrs = type.__prepare__()

# Step 2
body = """
def __init__(self, name):
    self.name = name

def say_hello(self):
    print("Hello {0}".format(self.name))
"""

# Step 3
exec(body, globals(), clsattrs)

# Step 4

Spam = type("Spam", (object,), clsattrs)



