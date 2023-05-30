#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = map(int, numbers)
    
    numbers = map(lambda x: x*x, numbers)
    
    print(numbers)
    
