#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = list(sys.argv[1])
    
    words.sort()
    
    print("\n".join(words))
    
