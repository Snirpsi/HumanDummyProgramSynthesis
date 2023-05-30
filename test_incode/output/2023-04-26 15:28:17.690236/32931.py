#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or stores words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    for word in words:
        print(word)
        
