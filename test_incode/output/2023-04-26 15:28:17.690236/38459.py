#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    total = 0
    for number in numbers:
        total += int(number)
    
    print('The total is %d' % total)
    
