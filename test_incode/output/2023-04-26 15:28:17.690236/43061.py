#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and iterates over user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    for word in words:
        print("%s: %s" % (word, word