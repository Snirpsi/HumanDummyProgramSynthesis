#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and prints words. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(str(i))
    
    print(" ".join(words))
    
