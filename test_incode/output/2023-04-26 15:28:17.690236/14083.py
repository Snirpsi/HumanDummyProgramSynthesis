#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = open(sys.argv[1]).read().split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) > 0]
    
    words = [word for word in words if word not in stopwords.words('english')]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in 