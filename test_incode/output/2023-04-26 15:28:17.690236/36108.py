#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers and multiplyes a list of words. """    
    numbers = [int(i) for i in input().split()]
    words = [input().split() for i in input().split()]
    
    numbers = list(map(lambda x: x * words[x], numbers))
    
    print(" ".join(map(str, numbers)))
    
