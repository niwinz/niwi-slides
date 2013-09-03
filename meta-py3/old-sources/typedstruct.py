# -*- coding: utf-8 -*-

def _make_init_code(fields):
    code = ["def __init__(self, {0}):\n".format(", ".join(fields))]
    for field in fields:
        code.append("    self.{0} = {0}\n".format(field))

    return "".join(code)


def _make_setter_code(descriptor):
    code = ["def __set__(self, instance, value):"]

    for cls in descriptor.__mro__:
        if "code" in cls.__dict__:
            for line in cls.code():
                code.append("    " + line)
    return "\n".join(code)


class DescriptorMeta(type):
    def __init__(cls, name, bases, attrs):
        if "__set__" not in attrs:
            exec(_make_setter_code(cls), globals(), attrs)
            setattr(cls, "__set__", attrs["__set__"])
        return super().__init__(name, bases, attrs)



class Descriptor(object, metaclass=DescriptorMeta):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    @staticmethod
    def code():
        return ["instance.__dict__[self.name] = value"]

    def __delete__(self, instance):
        del instance.__dict__[self.name]



class TypedDescriptor(Descriptor):
    _type = object

    @staticmethod
    def code():
        return ["if not isinstance(value, self._type):",
                "    raise TypeError('Expected {0}'.format(self._type))"]


class String(TypedDescriptor):
    _type = str


class Integer(TypedDescriptor):
    _type = int


class Positive(Descriptor):
    @staticmethod
    def code():
        return ["if value < 0:",
                "    raise ValueError('Expected >= 0')"]


class PositiveInteger(Integer, Positive):
    pass



from collections import OrderedDict

class StructMeta(type):
    @classmethod
    def __prepare__(cls, *args, **kwargs):
        return OrderedDict()

    def __new__(clst, name, bases, attrs):
        fields = [k for k,v in attrs.items()
                    if isinstance(v, Descriptor)]

        if fields:
            exec(_make_init_code(fields), globals(), attrs)

        for name in fields:
            attrs[name].name = name

        cls = super().__new__(clst, name, bases, attrs)
        cls._fields = fields
        return cls


class Struct(object, metaclass=StructMeta):
    pass
