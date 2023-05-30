#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    while True:
        numbers = [int(i) for i in input().split()]
        numbers = [n * n for n in numbers]
        print(' '.join(map(str, numbers)))
