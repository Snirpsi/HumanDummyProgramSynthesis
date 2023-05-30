#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = sorted(words, key=len, reverse=True)
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if len(w) > 2]
    
    words = [w for w in words if len(w) > 3]
    
    words = [w for w in words if len(w) > 4]
    
    words = [w for w in words if len(w) > 5]
    
    words = [w for w in words if len(w) > 6]
    
    words = [w for w in words if len(w) > 7]
    
    words = [w for w in words if len(w) > 8]
    
    words = [w for w in words if len(w) > 9]
    
    words = [w for w in words if len(w) > 10]
    
    words = [w for w in words if len(w) > 11]
    
    words = [w for w in words if len(w) > 12]
    
    words = [w for w in words if len(w) > 13]
    
    words = [w for w in words if len(w) > 14]
    
    words = [w for w in words if len(w) > 15]
    
    words = [w for w in words if len(w) > 16]
    
    words = [w for w in words if len(w) > 17]
    
    words = [w for w in words if len(w) > 18]
    
    words = [w for w in words if len(w) > 19]
    
    words = [w for w in words if len(w) > 20]
    
    words = [w for w in words if len(w) > 21]
    
    words = [w for w in words if len(w) > 22]
    
    words = [w for w in words if len(w) > 23]
    
    words = [w for w in words if len(w) > 24]
    
    words = [w for w in words if len(w) > 25]
    
    words = [w for w in words if len(w) > 26]
    
    words = [w for w in words if len(w) > 27]
    
    words = [w for w in words if len(w) > 28]
    
    words = [w for w in words if len(w) > 29]
    
    