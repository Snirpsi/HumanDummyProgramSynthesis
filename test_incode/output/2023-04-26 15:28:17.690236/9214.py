#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and multiplyes words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = words + line.split()
    
    words.sort()
    
    for word in words:
        print(word*2)
    
