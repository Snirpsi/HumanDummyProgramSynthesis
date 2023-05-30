#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and adds user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if len(words) == 