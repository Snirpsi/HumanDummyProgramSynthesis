#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    numbers = [int(x) for x in input().split()]
    print(*numbers, sep='\n')
