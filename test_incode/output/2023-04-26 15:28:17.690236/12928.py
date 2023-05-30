#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world']
    
    for word in words:
        print(word)
        
