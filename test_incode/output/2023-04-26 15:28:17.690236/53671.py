#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers or converts a list of words. """    
    
    import sys
    
    numbers = []
    
    for line in sys.stdin:
        numbers.append(int(line))
    
    numbers = 