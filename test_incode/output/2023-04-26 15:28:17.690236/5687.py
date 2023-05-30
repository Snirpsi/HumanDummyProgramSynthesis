#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    import sys
    
    words = sys.argv[1:]
    
    multiplied = 0
    for word in words:
        multiplied += word
    
    print(multiplied)
    
