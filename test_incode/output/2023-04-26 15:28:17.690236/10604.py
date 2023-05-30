#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    numbers = [int(n) for n in input().split()]
    
    total = sum(numbers)
    
    print("The total is {}".format(total))
    
