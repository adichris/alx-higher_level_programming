#!/usr/bin/python3
from typing import Any


class LockedClass(object):
    first_name = ""
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '%s'" % __name)
        else:
            super.__setattr__(self, __name, __value)