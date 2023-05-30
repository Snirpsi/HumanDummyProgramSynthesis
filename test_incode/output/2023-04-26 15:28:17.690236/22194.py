#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    wordlist.sort()
    for word in wordlist:
        print(word)

<|/ file filename=wordlist.py |>