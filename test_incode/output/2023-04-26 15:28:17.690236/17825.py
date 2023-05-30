#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words. """    
    import sys
    words = []
    for word in sys.stdin:
        words.append(word.strip())
    print(" ".join(words))
    
