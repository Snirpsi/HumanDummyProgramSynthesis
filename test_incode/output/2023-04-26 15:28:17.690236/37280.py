#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers. """    
    numbers = [int(n) for n in input().split()]
    print(sum(numbers))
    
