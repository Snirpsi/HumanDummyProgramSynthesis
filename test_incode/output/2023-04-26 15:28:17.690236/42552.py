#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and returns fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = []
    
    for i in range(1, 