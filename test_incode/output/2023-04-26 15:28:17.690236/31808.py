#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    print("Content-Type: text/plain")
    print("\n")
    
    for word in words:
        print("%s: %s" % (word, word))
        
    print("\n")
    
