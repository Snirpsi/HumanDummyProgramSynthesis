#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1].split()
    
    words = [x.lower() for x in words]
    
    words = [x for x in words if len(x) > 0]
    
    words = [x for x in words if x not in stopwords]
    
    words = [x for x in words if x not in punctuations]
    
    words = [x for x in words if x not in numbers]
    
    words = [x for x in words if x not in letters]
    
    words = [x for x in words if x not in symbols]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in words]
    
    words = [x for x in words if x not in word