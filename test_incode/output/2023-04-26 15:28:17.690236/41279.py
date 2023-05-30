#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers. """    
    
    import sys
    
    numbers = []
    
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers = numbers * 2
    
    print(' '.join(map(str, numbers)))
    
