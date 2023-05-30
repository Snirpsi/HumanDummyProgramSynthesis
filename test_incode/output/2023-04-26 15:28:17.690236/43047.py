#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    while True:
        numbers = [int(i) for i in input().split()]
        numbers = list(map(lambda x: x*x, numbers))
        print(*numbers, sep='