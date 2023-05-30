#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = list(filter(None, words))
    
    words.sort()
    
    for word in words:
        print("%s -> %s" % (word, word