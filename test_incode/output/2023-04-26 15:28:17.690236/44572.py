#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers. """    
    while True:
        numbers = [int(i) for i in input('Enter numbers: ').split()]
        numbers = [x * y for x, y in zip(numbers, numbers)]
        print(' '.join(map(str, numbers)))
        
