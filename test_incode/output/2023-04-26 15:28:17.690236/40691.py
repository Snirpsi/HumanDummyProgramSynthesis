#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers. """    
    import sys
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    print(numbers)
    
