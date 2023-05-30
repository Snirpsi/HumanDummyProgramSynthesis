#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and prints a list of words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Print words and list of words
    for word in words:
        print(word)
        print(