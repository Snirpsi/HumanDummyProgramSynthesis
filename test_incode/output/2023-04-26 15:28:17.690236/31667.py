#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers and returns a list of words. """    
    numbers = [int(x) for x in input().split()]
    words = []
    for number in numbers:
        words.append(str(number))
    print(" ".join(words))
    
