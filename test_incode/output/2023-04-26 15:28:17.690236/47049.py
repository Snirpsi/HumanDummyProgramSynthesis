#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in stop_words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if len(word) > 1]
    
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
    
    word