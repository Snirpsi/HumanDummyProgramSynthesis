#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        fruits = sys.argv[1:]
    else:
        fruits = ['apple', 'banana', 'cherry']
    
    fruits.sort()
    
    for fruit in fruits:
        print('{}: {}'.format(fruit, 