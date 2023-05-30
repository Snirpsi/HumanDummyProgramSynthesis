#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and calculates numbers. """    
    words = []
    numbers = []
    while True:
        words.append(input('Enter a word: '))
        numbers.append(int(input('Enter a number: ')))
        if len(words) == 