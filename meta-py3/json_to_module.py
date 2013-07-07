# -*- coding: utf-8 -*-

import json
import io


def _json_struct_to_code(struct):
    code = ["class {0}(_ts.Strict):".format(struct["name"])]
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
