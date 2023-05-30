#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and adds words. """    
    import sys
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    for word in words:
        print(word)
    
