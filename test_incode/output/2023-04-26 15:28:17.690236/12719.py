#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and stores a port. """    
    import sys
    port = int(sys.argv[1])
    words = []
    for word in sys.argv[2:]:
        words.append(word)
    
    for word in words:
        print(word)
    
