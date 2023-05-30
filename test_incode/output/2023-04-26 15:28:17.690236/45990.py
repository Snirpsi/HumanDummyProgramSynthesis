#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    with open('words.txt') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    return words

<|/ file ext=.py filename=wordlist.py source=github |>