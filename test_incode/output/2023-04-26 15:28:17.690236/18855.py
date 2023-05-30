#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or multiplyes words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for n in range(port):
        words.append(str(n