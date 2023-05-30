#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words. """    
    import sys
    words = sys.argv[1:]
    
    words.sort()
    
    for word in words:
        print(word)

<|/ file ext=.py |>