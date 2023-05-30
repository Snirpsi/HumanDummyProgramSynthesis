#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words = words + line.split()
        
    words.sort()
    
    for word in words:
        print(word)
        
