#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or returns words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    if len(words) == 0:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit(1)
    
    words = list(set(words))
    
    if len(words) > 100:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    if len(words) == 0:
        print("No words found")
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 2]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 3]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 4]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 5]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 6]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 7]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 8]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 9]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 10]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 11]
    
    if len(words) == 0:
        print("Too many words: %s" % " ".join(words))
        sys.exit(1)
    
    words.sort()
    
    words = [w for w in words if len(w) > 