#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    numbers.sort()
    
    sys.stdout.write("\n".join(map(str, numbers)))
    
