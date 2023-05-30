#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) > 0:
            words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
