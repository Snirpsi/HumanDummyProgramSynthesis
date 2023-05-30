#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    while True:
        numbers = [int(x) for x in input('Enter numbers: ').split()]
        numbers = [x * y for x, y in zip(numbers, numbers)]
        print(' '.join(map(str, numbers)))
