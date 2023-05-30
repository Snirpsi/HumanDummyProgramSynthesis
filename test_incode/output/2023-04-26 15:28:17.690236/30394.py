#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the file name: ")
    
    with open(filename) as file:
        words = file.read().split()
    
    words = [word.lower() for word in words]
    
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
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
