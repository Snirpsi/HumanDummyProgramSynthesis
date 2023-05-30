#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or multiplyes a list of numbers. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    numbers = []
    
    for arg in sys.argv[2:]:
        numbers.append(int(arg))
    
    numbers = numbers * 