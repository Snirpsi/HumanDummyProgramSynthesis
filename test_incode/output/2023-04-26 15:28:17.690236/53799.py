#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    while True:
        numbers = [int(i) for i in input().split()]
        if sum(numbers) == 