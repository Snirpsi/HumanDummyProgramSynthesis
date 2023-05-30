#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and returns fruits. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    fruits = []
    for word in words:
        fruits.append(word.upper())
    
    print(fruits)
    
