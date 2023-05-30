#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    
    import sys
    
    numbers = []
    
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers = list(map(int, numbers))
    
    numbers = sorted(numbers)
    
    numbers_str = ' '.join(map(str, numbers))
    
    print(numbers_str)
    
