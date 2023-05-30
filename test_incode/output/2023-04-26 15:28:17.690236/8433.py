#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and converts words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
        
    words = filter(None, words)
    
    words = map(str.lower, words)
    
    words = map(str.title, words)
    
    words = map(str.capitalize, words)
    
    words = map(str.swapcase, words)
    
    words = map(str.maketrans, words, 