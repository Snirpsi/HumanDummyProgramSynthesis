#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and removes user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if len(words) == 