#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers. """    
    
    numbers = [int(n) for n in input().split()]
    
    sum = 0
    
    for n in numbers:
        sum += n
    
    print(sum)
    
