#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or returns words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 80
    
    words = []
    
    for i in range(0, port):
        words.append(i)
    
    print(" ".join(words))
    
