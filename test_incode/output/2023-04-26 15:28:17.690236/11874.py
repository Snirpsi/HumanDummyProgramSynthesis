#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or converts a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    words = list(map(str.strip, words))
    
    words.sort()
    
    for word in words:
        print(word)
    
