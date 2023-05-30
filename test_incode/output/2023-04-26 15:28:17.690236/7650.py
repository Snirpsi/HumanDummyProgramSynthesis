#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        print('{}: {}'.format(fruit, 