#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    while True:
        numbers = [int(n) for n in input().split()]
        numbers.reverse()
        print(*numbers)
        
