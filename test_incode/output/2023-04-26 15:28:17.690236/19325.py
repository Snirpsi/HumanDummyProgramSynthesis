#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    numbers_converted = [str(n) for n in numbers]
    
    print(numbers_converted)
    
