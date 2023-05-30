#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of numbers and opens a list of words. """    
    numbers = [int(x) for x in input().split()]
    words = [x.capitalize() for x in input().split()]
    print(*numbers, sep=", ")
    print(*words, sep=", ")
    
