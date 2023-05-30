#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    for word in words:
        
        if word not in words:
            print(word)
    
