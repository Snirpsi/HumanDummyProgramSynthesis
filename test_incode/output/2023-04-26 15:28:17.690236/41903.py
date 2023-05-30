#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    numbers = [int(n) for n in input().split()]
    
    while(True):
        
        numbers.append(int(input()))
        
        