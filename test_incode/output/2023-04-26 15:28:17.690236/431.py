#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and prints a list of words. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        if line[0] == '#':
            continue
        
        words.append(line)
    
    for word in words:
        print(word)
        
