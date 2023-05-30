#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and stores words. """    
    numbers = [int(i) for i in input().split()]
    words = [str(num) for num in numbers]
    print(" ".join(words))
    
