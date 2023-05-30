#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port or returns words. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(sys.stdin.readline())
    
    print(" ".join(words))
    
