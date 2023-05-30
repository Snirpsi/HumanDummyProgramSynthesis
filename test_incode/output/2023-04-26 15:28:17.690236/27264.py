#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    while True:
        numbers = [int(i) for i in input().split()]
        if len(numbers) == 0:
            break
        print(*numbers, sep='