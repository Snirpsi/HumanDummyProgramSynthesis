#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = words.split()
    
    for word in words:
        print(word)
        
