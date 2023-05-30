#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    words = [w for w in sys.argv[1:] if w != '--help']
    
    for word in words:
        
        if word in sys.argv:
            sys.argv.remove(word)
            
    print(sys.argv)
    
