#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = list(map(int, numbers))
    
    for number in numbers:
        print(number)
    
