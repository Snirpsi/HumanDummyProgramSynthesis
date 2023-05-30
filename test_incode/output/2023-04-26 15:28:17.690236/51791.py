#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or converts all ports. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    words = word