#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or enumerates user input. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words.sort()
    
    for word in words:
        print("%s: %s" % (word, word))
    
