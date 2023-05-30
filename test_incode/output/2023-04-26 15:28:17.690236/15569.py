#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and iterates over words. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if len(words) == 