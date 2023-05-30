#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns fruits or stores a port. """    
    
    fruits = fruits_or_store()
    
    if fruits is not None:
        for fruit in fruits:
            print(