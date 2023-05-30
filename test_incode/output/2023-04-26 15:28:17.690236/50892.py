#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers. """    
    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    total = 0
    
    for n in numbers:
        total += n
    
    print(total)
    
