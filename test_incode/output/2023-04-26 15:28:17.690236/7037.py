#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and enumerates words. """    
    numbers = input("Enter a list of numbers: ")
    words = enumerate(numbers.split())
    for index, word in words:
        print(index, word)
