#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and returns fruits. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    fruits = []
    for word in words:
        fruits.append(word