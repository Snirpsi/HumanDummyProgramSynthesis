#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words and enumerates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        exit(1)
    
    port = sys.argv[1]
    
    words = []
    
    words = enumerateWords(port)
    
    for word, count in words:
        print("%s: %d" % (word, count))
    
