#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of numbers or multiplyes a list of words. """    
    
    numbers = [int(i) for i in input().split()]
    words = [input().split() for i in input().split()]
    
    words = [