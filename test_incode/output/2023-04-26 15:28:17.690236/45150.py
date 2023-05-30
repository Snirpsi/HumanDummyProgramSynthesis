#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        numbers.append(int(line))
    
    numbers.sort()
    
    for number in numbers:
        print(number)
    
