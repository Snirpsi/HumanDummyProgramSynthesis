#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    while True:
        word = input("Enter a word: ")
        word_length = len(word)
        
        if word_length == 0 or word_length == 