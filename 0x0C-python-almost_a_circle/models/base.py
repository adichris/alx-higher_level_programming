#!/usr/bin/python3
""" Base Class """


class Base:
    """ base class"""
    __nb_objects = 0
    
    def __init__(self, id=None) -> None:
        """base constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
