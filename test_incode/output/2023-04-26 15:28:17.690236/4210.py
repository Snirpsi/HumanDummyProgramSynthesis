#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    with open(sys.argv[1]) as f:
        words = [word.strip() for word in f]
    
    words.sort()
    
    for word in words:
        print(word)

<|/ file filename=wordlist.py ext=.py |>