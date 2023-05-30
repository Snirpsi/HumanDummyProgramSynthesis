#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or calculates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        if len(words) == 1:
            
            word = "1"
            
        else:
            
            word = "