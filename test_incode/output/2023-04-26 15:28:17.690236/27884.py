#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and multiplyes fruits. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    fruits = []
    
    for number in numbers:
        fruits.append(number * 2)
    
    print('\n'.join(map(str, fruits)))
    
