#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words. """    
    words = []
    
    # Read all words from file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Remove duplicates
    words = list(set(words))
    
    # Print the words in reverse order
    for word in reversed(words):
        print(word)
    
