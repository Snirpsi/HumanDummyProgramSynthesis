#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers. """    
    while True:
        numbers = [int(i) for i in input().split()]
        if numbers == []:
            break
        print(*numbers, sep='