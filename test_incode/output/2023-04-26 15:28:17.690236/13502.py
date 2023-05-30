#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    for number in numbers:
        print(number)
    
