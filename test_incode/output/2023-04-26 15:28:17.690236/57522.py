#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s word1 word2 word3 ..." % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1:]]
    
    if len(words) == 0:
        print("Usage: %s word1 word2 word3 ..." % sys.argv[0])
        sys.exit()
    
    words = [w.lower() for w in words]
    
    multiplied = 0
    
    for word in words:
        multiplied += word