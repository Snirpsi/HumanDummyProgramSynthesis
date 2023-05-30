#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers. """    
    while True:
        numbers = [int(i) for i in input().split()]
        print(*numbers, sep='