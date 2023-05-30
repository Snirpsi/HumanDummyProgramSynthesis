#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and converts a list of words. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for c in sys.stdin:
        words.append(c.strip())
    
    words = words.split()
    
    for word in words:
        print(word