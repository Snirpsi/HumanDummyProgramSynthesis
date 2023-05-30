#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and returns a port. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    port = int(sys.argv[1])
    
    for word in words:
        if word in port