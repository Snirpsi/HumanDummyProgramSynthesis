#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers and prints a list of numbers. """    
    while True:
        numbers = [int(x) for x in input().split()]
        print(*numbers, sep='\n')
        
