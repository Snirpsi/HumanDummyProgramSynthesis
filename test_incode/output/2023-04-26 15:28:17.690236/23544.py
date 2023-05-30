#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    words.sort()
    word