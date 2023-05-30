#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or opens words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 2]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 3]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 4]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 5]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 6]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 7]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 8]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 9]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 10]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 11]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 12]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 13]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 14]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 15]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 16]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 17]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 18]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 19]
    
    words = [word for word in words if word not in STOPWORDS and len(word) > 20