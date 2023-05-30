#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits and multiplyes a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_multiplied = []
    
    for fruit in fruits:
        fruits_multiplied.append(fruit*