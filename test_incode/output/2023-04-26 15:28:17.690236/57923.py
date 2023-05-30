#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    return words

<|/ file ext=.py source=github |>