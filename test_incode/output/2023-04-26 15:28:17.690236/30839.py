#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or returns a list of words. """    
    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('\n'.join(words))

<|/ file ext=.py |>