# -*- coding: utf-8 -*-

import json
import imp
import io
import os
import sys


def _json_struct_to_code(struct):
    code = ["class {0}(_ts.Struct):".format(struct["name"])]
    for field in struct["fields"]:
        c = "{0} = _ts.{1}()".format(field["name"],
                                     field["type"])
        code.append("    " + c)
    return code


def _json_to_code(filename):
    with io.open(filename, "rt") as f:
        data = json.load(f)

    code = ["import typedstruct as _ts"]
    for struct in data:
        code.extend(_json_struct_to_code(struct))
    return "\n".join(code)


class StructImporter(object):
    def __init__(self, path):
        self._path = path

    def find_module(self, fullname, path=None):
        name = fullname.partition(".")[0]
        if path is None:
            path = self._path

        for dir in path:
            final_name = os.path.join(dir, "{0}.json".format(name))
            if os.path.exists(final_name):
                return JsonLoader(final_name)

        return None


class JsonLoader(object):
    def __init__(self, filename):
        self._filename = filename

    def load_module(self, fullname):
        mod = imp.new_module(fullname)
        mod.__file__ = self._filename
        mod.__loader__ = self

        code = _json_to_code(self._filename)
        exec(code, mod.__dict__, mod.__dict__)
        sys.modules[fullname] = mod
        return mod


def install_importer():
    sys.meta_path.append(StructImporter(sys.path))

install_importer()
