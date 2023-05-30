#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words. """    
    import sys
    words = []
    for word in sys.stdin:
        words.append(word.strip())
    print(" ".join(words))
