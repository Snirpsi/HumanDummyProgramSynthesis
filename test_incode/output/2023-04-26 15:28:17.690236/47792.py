#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers. """    
    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    for n in numbers:
        print(n)
    
