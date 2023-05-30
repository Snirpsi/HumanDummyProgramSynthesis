#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    numbers = [int(n) for n in input().split()]
    print(*numbers, sep='\n')