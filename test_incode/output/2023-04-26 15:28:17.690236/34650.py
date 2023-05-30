#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and removes a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    print(" ".join(wordlist))

<|/ file ext=.py |>