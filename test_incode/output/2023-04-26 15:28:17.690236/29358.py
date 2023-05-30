#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').lower())
        if words[-1] == 'q':
            break
    return words

<|/ file filename=wordlist.py ext=.py |>