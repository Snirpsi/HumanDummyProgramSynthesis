#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or returns a port. """    
    import sys
    port = int(sys.argv[1])
    
    for word in words:
        print(word, port)
        port += 1
    
