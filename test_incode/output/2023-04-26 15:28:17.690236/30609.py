#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input and enumerates words. """    
    
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
    
    
