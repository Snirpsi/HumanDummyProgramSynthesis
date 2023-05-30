#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of numbers and prints a list of words. """    
    numbers = [int(i) for i in input("Enter a number: ").split()]
    words = [str(n) for n in numbers]
    print(" ".join(words))
