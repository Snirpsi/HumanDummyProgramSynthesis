#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or opens words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split()]
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [w.lower() for w in words]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS]
    
