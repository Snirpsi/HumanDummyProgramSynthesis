#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or iterates over a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip())
        if words:
            break
    return words

<|/ file ext=.py |>