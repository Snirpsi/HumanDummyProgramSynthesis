#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and prints a list of numbers. """    
    import sys
    words = [line.strip() for line in sys.stdin]
    numbers = [int(word) for word in words]
    
    print('\n'.join(map(str, numbers)))
    
