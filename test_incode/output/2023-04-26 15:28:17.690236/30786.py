#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    with open(sys.argv[1]) as f:
        words = f.read().splitlines()
    
    words = [word.strip() for word in words]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 1]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 1]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 1]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
