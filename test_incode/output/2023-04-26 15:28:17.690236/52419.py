#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and enumerates fruits. """    
    
    import sys
    
    words = []
    fruits = []
    
    for arg in sys.argv[1:]:
        words = words + arg.split(' ')
    
    for word in words:
        fruits.append(word)
    
    fruits.sort()
    
    for fruit in fruits:
        print(fruit)
    
