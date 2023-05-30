#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers and calculates numbers. """    
    while True:
        numbers = [int(n) for n in input().split()]
        print(sum(numbers))
        
