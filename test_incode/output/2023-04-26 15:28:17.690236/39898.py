#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers. """    
    
    numbers = [int(i) for i in input().split()]
    
    total = 0
    
    for n in numbers:
        total += n
    
    print(total)
    
