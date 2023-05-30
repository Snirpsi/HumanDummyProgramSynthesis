#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        words.append(line)
    
    words.sort()
    
    words = [w for w in words if w not in words]
    
    print("\n".join(words))
    
