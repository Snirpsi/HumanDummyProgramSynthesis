#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and returns numbers. """    
    
    import sys
    
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    numbers.sort()
    
    print(numbers)
    
