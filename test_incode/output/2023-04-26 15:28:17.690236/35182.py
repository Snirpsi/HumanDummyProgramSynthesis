#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [words]' % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    words = [w.lower() for w in words]
    
    words = [w for w in words if len(w) > 2]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if len(w) > 0]
    
    words = [w for w in words if w not in stopwords]
    
    words = [w for w in words if w not in punctuation]
    
    words = [w for w in words if w not in numbers]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
    words = [w for w in words if w not in words]
    
