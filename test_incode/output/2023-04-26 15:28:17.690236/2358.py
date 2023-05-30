#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words or adds user input. """    
    
    # Read user input
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    # Add user input
    words += 