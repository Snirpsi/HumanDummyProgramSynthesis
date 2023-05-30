#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    for word in words:
        print(word)

<|/ file filename=wordlist.py ext=.py |>