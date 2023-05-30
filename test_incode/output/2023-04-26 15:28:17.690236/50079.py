#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or stores a list of words. """    
    
    # Read user input
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'done':
            break
        words.append(word)
    
    # Store list of words
    word