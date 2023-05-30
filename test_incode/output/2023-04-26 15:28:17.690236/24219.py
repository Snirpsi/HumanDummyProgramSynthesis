#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers and enumerates words. """    
    numbers = [int(i) for i in input().split()]
    words = enumerate(numbers)
    print(*words, sep='\n')
    
