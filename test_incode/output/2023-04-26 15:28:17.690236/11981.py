#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or iterates over a list of numbers. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    i = 0
    while i < len(words):
        print(words[i], end=' ')
        i += 1
    
