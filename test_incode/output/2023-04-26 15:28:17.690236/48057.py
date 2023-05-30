#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <file>" % sys.argv[0])
        sys.exit(0)
    
    with open(sys.argv[1], 'r') as f:
        words = f.read().split()
    
    words = [w for w in words if w not in ['\n', '\r']]
    
    with open(sys.argv[1], 'w') as f:
        f.write(' '.join(words))
        
    print("Removed %d words from %s" % (len(words), sys.argv[1]))
    
