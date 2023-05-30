#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and enumerates a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    while True:
        words.append(str(port*