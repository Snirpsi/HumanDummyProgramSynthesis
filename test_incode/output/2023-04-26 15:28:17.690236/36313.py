#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    words = sys.argv[1:]
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)

<|/ file ext=.py |>