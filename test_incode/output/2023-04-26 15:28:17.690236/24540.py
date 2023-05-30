#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and calculates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = [w.lower() for w in words]
    
    words = [w for w in words if len(w) > 2]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if len(w) > 0]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS and w not in PUNCTUATION]
    
    words = [w for w in words if w not in STOPWORDS and w not in PUNCTUATION and w not in NUMBERS]
    
    words = [w for w in words if w not in STOPWORDS and w not in PUNCTUATION and w not in NUMBERS and w not in SYMBOLS]
    
    words = [w for w in words if w not in STOPWORDS]
    
    words = [w for w in words if w not in STOPWORDS and w not in PUNCTUATION and w not in NUMBERS and w not in SYMBOLS and w not in STOPWORDS]
    
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
    
    words = [w for 