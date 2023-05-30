#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or multiplyes fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    server