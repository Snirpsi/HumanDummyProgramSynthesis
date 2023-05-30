#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers and returns a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words:
            break
    return words

<|/ file source=github filename=