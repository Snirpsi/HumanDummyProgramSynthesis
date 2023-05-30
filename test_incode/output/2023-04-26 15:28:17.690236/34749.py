#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = [w for w in words if w]
    
    for word in words:
        
        if word not in ['.', '?', '!']:
            
            print(word)
            
        else:
            
            print(word)
            
            
