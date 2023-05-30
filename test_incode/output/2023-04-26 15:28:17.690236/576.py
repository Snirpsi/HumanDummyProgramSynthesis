#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words and enumerates user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if len(words) == 