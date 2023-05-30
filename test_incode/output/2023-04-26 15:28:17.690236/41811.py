#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or enumerates fruits. """    
    
    import sys
    
    words = []
    fruits = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(sys.argv) > 2:
        fruits = sys.argv[2:]
    
    words.sort()
    fruits.sort()
    
    for word in words:
        print(word)
    
    for fruit in fruits:
        print(fruit)
    
