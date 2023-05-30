#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or adds a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        for word in words:
            print(word)
            
    else:
        
        print('Usage: %s <words>' % sys.argv[0])
        
