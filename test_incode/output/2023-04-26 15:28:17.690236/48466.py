#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    numbers = [i for i in numbers if i!