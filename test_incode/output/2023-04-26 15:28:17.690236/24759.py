#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    print(" ".join(words))

<|/ file source=github ext=.py |>