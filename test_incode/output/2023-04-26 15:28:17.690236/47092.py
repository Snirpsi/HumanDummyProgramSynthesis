#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and removes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1].split()
    
    words = [w.lower() for w in words]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if w not in STOPWORDS]
    
    print("\n".join(words))
    
