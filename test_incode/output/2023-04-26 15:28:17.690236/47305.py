#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [word.strip() for word in sys.argv[1].split(',')]
    
    words.sort()
    
    words = [word.upper() for word in words]
    
    print(",".join(words))
    
