#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port and iterates over words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(sys.argv[2])
        
    print(" ".join(words))
    
