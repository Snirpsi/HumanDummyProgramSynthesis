#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for 