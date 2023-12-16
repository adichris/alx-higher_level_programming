#!/usr/bin/python3
""" Base Class """


class Base:
    __nb_objects = 0
    id = 0
    def __init__(self, id=None) -> None:
        if id:
            self.id = id
        else:
            Base.id += 1
