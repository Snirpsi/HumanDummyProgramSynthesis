#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and opens a list of numbers. """    
    
    words = open('words.txt').read().splitlines()
    numbers = open('numbers.txt').read().splitlines()
    
    for word in words:
        number = number