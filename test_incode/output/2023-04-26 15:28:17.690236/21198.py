#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or multiplyes a list of words. """    
    import sys
    port = int(sys.argv[1])
    words = []
    for x in range(port):
        words.append(str(x