#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or converts a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
