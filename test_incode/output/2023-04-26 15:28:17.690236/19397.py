#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    with open('./words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    return words

<|/ file ext=.py |>