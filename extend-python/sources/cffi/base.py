# -*- coding: utf-8 -*-

import api
import binascii

class sha256(object):
    _result = None

    def __init__(self, data=None):
        self.td = api.lib.mhash_init(17)
        if not isinstance(data, bytes):
                raise RuntimeError("data must be bytes instance")

        _data = api.ffi.new("char[]", data)
        api.lib.mhash(self.td, _data, len(data))

    def digest(self):
        if self._result is not None:
            return binascii.hexlify(self._result)

        _size = api.lib.mhash_get_block_size(17)
        _result = api.lib.mhash_end(self.td)
        self._result = api.ffi.buffer(_result, _size)
        return binascii.hexlify(self._result)
