#!/usr/bin/python3
'''
    Creating the base class of all other classes for this project.
'''

Class Base:
    '''
        This class will manage the id attribute for all the classes.
        Arguments:
            @id: The id for a specific instance.
    '''
    __nb_objects = 0
    def __init__(self, id=None):
        if id!=None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
