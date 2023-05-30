#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
        
