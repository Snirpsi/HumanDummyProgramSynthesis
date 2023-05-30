#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    for word in words:
        print(word)
        
