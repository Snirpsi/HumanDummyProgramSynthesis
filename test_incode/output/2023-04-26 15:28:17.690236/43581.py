#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers. """    
    numbers = [int(x) for x in input().split()]
    numbers += numbers[:1]
    numbers += numbers[-1:]
    print(*numbers, sep='