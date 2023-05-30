#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words. """    
    import sys
    words = []
    for word in sys.stdin:
        words.append(word.strip())
    
    for word in words:
        print(word)

<|/ file filename=wordlist.py ext=.py |>