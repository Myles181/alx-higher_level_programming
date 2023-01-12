#!/usr/bin/python3
'''
class Base
'''
class Base:
    '''
    private instance attribute
    '''
    __nb_objects = 0
    '''
    Initialize new Base
    Args:
        id(int): The identity of the new Base
    '''
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
