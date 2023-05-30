#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and stores user input. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if len(words) == 