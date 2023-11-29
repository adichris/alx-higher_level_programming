#!/usr/bin/python3


class Square:
    """ a class that defines private instance variables"""

    _Square__size = None

    def __init__(self, size=0):
        self._Square__size = size
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))