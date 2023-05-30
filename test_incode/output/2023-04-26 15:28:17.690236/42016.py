#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words and prints a port. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    print(" ".join(words))

<|/ file ext=.py source=github |>