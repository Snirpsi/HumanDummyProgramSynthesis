#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
    
    words.sort()
    
    sys.stdout.write(' '.join(words))
    
