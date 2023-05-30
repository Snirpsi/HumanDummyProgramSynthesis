#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    total = 0
    for word in words:
        total += word