#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <list.txt>" % sys.argv[0])
        sys.exit()
    
    words = []
    
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['\n', '\t']]
    
    words = list(set(words))
    
    words.sort()
    
    