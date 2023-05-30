#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and multiplyes a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = [int(n) for n in sys.argv[2:]]
    
    numbers_iter = iter(numbers)
    
    for number in numbers_iter:
        number *= next(numbers_iter)
    
    print(numbers)
    
