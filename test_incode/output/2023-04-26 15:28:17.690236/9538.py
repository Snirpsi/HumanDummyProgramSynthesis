#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or iterates over words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = list(filter(None, words))
    
    words.sort()
    
    sys.stdout.write("\n".join(words))
    
