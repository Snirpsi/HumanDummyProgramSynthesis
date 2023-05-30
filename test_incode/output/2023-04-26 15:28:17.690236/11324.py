#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and stores a port. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    port = 0
    for word in words:
        port *= int(word)
    
    print(port)
    
