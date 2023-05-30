#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
        
