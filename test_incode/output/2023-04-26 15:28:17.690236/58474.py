#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').title())
        if len(words) == 