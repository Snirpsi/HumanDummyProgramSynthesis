#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words.sort()
    
    print('\n'.join(words))
    
