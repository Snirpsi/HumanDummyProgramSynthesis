#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = list()
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.rstrip())
    return words

<|/ file ext=.py source=github |>