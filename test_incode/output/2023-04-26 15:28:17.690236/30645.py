#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and opens user input. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split()
        
        if len(words) == 0:
            continue
        
        words.sort()
        
        for word in words:
            print(word)
    
