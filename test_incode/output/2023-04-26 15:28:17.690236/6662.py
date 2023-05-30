#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or multiplyes fruits. """    
    
    import sys
    
    fruits = sys.argv[1:]
    
    if len(fruits) == 0:
        print("Usage: python server.py fruits")
        sys.exit(1)
    
    fruits = list(fruits)
    
    server