#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and adds a list of words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if len(words) == 