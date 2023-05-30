#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words. """    
    import sys
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    for word in words:
        print(word)
