#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers_converted = []
    for number in numbers:
        numbers_converted.append(int(number))
    
    print(numbers_converted)
    
