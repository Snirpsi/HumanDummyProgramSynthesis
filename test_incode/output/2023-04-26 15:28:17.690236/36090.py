#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and iterates over words. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
        
    words = filter(None, words)
    
    for word in words:
        print(word)
    
