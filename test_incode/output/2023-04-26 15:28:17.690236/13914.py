#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and multiplyes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    fruits_multiplied = []
    
    for fruit in fruits:
        fruits_multiplied.append(fruit*2)
    
    print('\n'.join(fruits_multiplied))
    
