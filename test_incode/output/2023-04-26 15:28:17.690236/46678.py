#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and enumerates a port. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    port = 0
    
    for word in words:
        port *= int(word)
    
    print(port)
    
