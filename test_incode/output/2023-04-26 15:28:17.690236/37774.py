#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        
        if word not in ['-', '--']:
            
            print(word)
            
        else:
            
            sys.exit()
            
