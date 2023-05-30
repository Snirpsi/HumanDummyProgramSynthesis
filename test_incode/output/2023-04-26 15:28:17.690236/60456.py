#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and removes numbers. """    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    words = list(set(words))
    words.sort()
    return words

<|/ file ext=.py filename=wordlist.py |>