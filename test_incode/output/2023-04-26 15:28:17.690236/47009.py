#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: enumerate.py <words>")
        sys.exit(1)
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
