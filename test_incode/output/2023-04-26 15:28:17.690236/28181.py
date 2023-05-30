#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    while True:
        numbers = [int(x) for x in input().split()]
        numbers = [x*x for x in numbers]
        print(*numbers, sep=', ')
