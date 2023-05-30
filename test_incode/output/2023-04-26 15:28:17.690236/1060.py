#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and adds a list of words. """    
    
    # Read user input
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    print('\n'.join(words))
    
