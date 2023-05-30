#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and stores words. """    
    numbers = open('numbers.txt')
    words = open('words.txt', 'w')
    
    for line in numbers:
        word