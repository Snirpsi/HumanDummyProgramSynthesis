#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and converts a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuations]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]