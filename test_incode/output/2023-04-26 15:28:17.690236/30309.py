#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = words + line.split()
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if len(word) > 1]
    
    print(" ".join(words))
    
