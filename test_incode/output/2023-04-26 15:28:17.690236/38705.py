#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers and calculates words. """    
    numbers = [int(i) for i in input().split()]
    words = [str(n) for n in numbers]
    print(" ".join(words))

<|/ file filename=