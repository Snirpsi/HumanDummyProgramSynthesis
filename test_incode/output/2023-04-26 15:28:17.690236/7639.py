#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(-1)
    
    words = sys.argv[1].split()
    
    words.sort()
    
    for word in words:
        print("%s %s" % (word, 