#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers and stores a list of words. """    
    
    numbers = [int(x) for x in input().split()]
    
    words = []
    
    for number in numbers:
        words.append(str(number))
    
    print(" ".join(words))
    
