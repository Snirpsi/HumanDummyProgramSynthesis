#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = words + line.split()
    
    for word in words:
        print(word)
        
