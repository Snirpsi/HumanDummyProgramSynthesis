#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    words = [w for w in sys.argv[1:] if w.strip()]
    
    if len(words) == 0:
        print("No words given.")
    else:
        print("Removing words from 