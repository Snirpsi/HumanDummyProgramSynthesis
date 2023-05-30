#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or opens a list of words. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        if line[0] == '#':
            continue
        
        if line[0] == '-':
            continue
        
        if line[0] == '+':
            words.append(line[1:])
            continue
        
        if line[0] == '"':
            words.append(line[1:-1])
            continue
        
        words = words + line.split(' ')
        
    words.sort()
    
    for word in words:
        print(word)
    
