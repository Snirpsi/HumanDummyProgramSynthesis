#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words = words + line.split()
    words.sort()
    for word in words:
        print(word)
