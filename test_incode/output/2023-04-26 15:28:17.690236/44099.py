#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <wordfile>" % sys.argv[0])
        sys.exit(0)
    
    wordfile = sys.argv[1]
    
    words = []
    
    with open(wordfile) as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    print("\n".join(words))
    
