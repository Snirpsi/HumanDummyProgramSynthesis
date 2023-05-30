#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input and removes words. """    
    
    import sys
    
    words = sys.stdin.read().split()
    
    for word in words:
        
        if word not in words:
            print(word)
    
    