#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and stores fruits. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    fruits = []
    
    for word in words:
        fruits.append(word)
    
    fruits.sort()
    
    for fruit in fruits:
        print("%s %s" % (fruit, len(word