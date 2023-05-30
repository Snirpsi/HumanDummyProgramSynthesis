#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit('Usage: %s <words>' % sys.argv[0])
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    words = [words[i:i+3] for i in range(0, len(words), 3)]
    
    words = [word for word in words if word]
    
    print('\n'.join(words))
    
