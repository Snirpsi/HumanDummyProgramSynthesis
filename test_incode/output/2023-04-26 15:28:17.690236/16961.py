#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
        
    print(" ".join(words))
    
