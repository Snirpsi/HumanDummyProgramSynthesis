#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and stores fruits. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    fruits = []
    for word in words:
        fruits.append(word)
    
    fruits = list(fruits)
    
    fruits.sort()
    
    fruits_str = ""
    for fruit in fruits:
        fruits_str += "%s " % fruit
    
    sys.stdout.write(fruits_str)
    sys.stdout.flush()
    
