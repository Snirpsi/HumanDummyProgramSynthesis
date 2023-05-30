#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
        
    words.sort()
    
    for line in words:
        print(line)
        
