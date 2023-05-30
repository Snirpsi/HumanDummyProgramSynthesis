#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or stores a list of words. """    
    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if len(words) == 