#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
