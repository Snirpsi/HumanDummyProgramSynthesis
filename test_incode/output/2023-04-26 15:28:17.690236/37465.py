#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and returns fruits. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
    
    fruits = []
    
    for word in words:
        fruits.append(word)
    
    words.sort()
    
    for fruit in fruits:
        print(fruit)
    
