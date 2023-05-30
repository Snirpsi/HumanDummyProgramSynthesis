#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    words = [word for word in words if word]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in 