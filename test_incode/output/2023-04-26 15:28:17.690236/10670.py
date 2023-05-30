#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers and opens a list of words. """    
    numbers = [int(n) for n in input().split()]
    words = [w for n in numbers for w in words if n % w == 0]
    print(*words, sep='\n')
