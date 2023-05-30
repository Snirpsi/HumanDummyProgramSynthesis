#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        for word in words:
            
            remove_port(word)
            
    else:
        
        remove_port('all')
        
        
