#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or prints fruits. """    
    import sys
    port = sys.argv[1]
    
    fruits = ['apple', 'banana', 'cherry']
    
    
    for fruit in fruits:
        print('