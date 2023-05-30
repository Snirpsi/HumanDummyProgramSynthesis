#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    import sys
    
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    print(*numbers, sep='\n')

<|/ file ext=.py filename=