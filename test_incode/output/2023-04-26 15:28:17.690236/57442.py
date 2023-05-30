#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and prints a list of words. """    
    numbers = [int(i) for i in input("Enter a list of numbers: ").split()]
    words = []
    for number in numbers:
        words.append(str(number))
    print(" ".join(words))
    
