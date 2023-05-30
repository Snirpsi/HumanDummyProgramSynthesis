#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: enumerate_words.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        print("%s: %s" % (word, 