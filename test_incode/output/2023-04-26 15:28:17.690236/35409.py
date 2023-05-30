#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        sys.stdout.write(word)
        sys.stdout.flush()
        
    if words[-1] == '':
        sys.stdout.write('\n')
    
    sys.stdout.write('\n')
    sys.stdout.flush()
    
    
