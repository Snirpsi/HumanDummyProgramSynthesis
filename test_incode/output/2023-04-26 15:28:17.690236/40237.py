#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
        
    words.sort()
    
    multiplied = []
    
    for word in words:
        multiplied.append(word[0] * word[1])
        
    print(" ".join(map(str, multiplied)))
    
