#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or stores a list of words. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
        
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
        
