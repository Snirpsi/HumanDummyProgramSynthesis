#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or stores all ports. """    
    import sys
    
    words = []
    ports = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(sys.argv) > 2:
        ports = sys.argv[2:]
    
    for word in words:
        for port in ports:
            print(word, port)
    
