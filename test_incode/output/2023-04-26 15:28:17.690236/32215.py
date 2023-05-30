#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers. """    
    
    import sys
    
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        numbers.append(int(line))
    
    print(numbers)

<|/ file source=github ext=.py filename=