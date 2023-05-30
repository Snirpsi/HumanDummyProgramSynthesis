#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or iterates over a list of words. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
    
