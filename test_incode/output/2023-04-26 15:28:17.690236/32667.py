#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    
    # read input from stdin
    numbers = map(int, sys.stdin.readline().split())
    
    # print output to stdout
    for n in numbers:
        print(n, end=' ')
    print()
    
