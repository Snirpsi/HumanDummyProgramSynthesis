#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and iterates over a list of words. """    
    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    for word in words:
        port *= int(word)
        
    print(port)
    
