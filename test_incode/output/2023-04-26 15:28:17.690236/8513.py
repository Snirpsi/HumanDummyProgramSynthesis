#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    words.sort()
    
    print("\n".join(words))
    
