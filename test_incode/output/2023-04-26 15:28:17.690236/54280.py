#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers. """    
    while True:
        numbers = [int(x) for x in input().split()]
        numbers = [x * y for x, y in zip(numbers, numbers[1:])]
        print(*numbers, sep='\n')
