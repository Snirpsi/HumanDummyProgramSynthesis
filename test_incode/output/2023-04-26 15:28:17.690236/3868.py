#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    print(words)

<|/ file ext=.py |>