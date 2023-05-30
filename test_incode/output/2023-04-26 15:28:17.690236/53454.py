#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        words = [word.strip() for word in f.readlines()]
        
    # Print all words
    for word in words:
        print(word)
        
    # Print all words with spaces in between
    for word in words:
        print(word.replace(" ", "