#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of numbers and prints a list of words. """    
    numbers = [int(i) for i in input().split()]
    words = [str(number) for number in numbers]
    print(" ".join(words))
    
