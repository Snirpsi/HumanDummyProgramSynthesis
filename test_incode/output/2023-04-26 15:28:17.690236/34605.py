#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    count = 0
    for word in words:
        if word not in words:
            count += 1
    
    print(count)
    
