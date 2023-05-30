#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    numbers = [int(x) for x in sys.stdin.readline().split()]
    
    for number in numbers:
        print(number)
        
    
