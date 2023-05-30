#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or opens fruits. """    
    
    import sys
    
    fruits = sys.argv[1:]
    
    if len(fruits) == 0:
        fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    
    for fruit in fruits:
        print('