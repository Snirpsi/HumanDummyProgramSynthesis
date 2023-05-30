#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or enumerates fruits. """    
    
    import sys
    
    fruits = ['apple', 'banana', 'cherry']
    
    if len(sys.argv) > 1:
        fruits = sys.argv[1:]
    
    for fruit in fruits:
        print('%s: %s' % (fruit, 