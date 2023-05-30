#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and calculates all ports. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    ports = []
    for word in words:
        ports.append(