#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit(0)
    
    words = list(words)
    
    words.sort()
    
    for word in words:
        print("%s: %s" % (word, word