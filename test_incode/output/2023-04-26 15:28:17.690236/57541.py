#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and converts words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    words.sort()
    print(words)

<|/ file ext=.py filename=wordlist.py |>