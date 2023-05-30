#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers and opens a list of words. """    
    numbers = input('Enter a number or words: ')
    words = input('Enter a words: ')
    
    numbers = numbers.split()
    words = words.split()
    
    numbers = list(map(int, numbers))
    words = list(map(