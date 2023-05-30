#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and iterates over a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = sys.argv[2:]
    
    numbers_iter = iter(numbers)
    
    for number in numbers_iter:
        print(number)
    
    