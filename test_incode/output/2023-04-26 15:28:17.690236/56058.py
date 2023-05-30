#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words. """    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    print(" ".join(words))

<|/ file ext=.py filename=wordlist.py |>