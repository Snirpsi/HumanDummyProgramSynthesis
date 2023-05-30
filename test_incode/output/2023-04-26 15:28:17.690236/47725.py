#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    import sys
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    total = 0
    for word in words:
        total += int(word) * int(word