#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    print("Adding words to %s..." % sys.argv[1])
    
    words = words.split()
    
    for word in words:
        word = "%s %s" % (word, word)
        
        print("  %s" % word)
        
    