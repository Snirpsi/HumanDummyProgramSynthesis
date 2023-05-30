#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and iterates over words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = list(sys.argv[1:])
    
    words.sort()
    
    for word in words:
        print("%s\t%s" % (word, 