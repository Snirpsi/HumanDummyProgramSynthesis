#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and returns fruits. """    
    
    numbers = range(1,100)
    fruits = []
    for number in numbers:
        fruits.append(number)
    
    print('\n'.join(map(str,fruits)))
    
