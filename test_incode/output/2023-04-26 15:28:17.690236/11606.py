#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    words.sort()
    
    for line in words:
        print(line)
    
