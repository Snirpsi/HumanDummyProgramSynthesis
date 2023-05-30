#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or prints a list of words. """    
    import sys
    port = int(sys.argv[1])
    words = []
    
    for i in range(port):
        words.append(str(i))
    
    print(" ".join(words))
    
