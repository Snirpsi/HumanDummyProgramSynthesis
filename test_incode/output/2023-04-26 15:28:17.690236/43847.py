#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words or removes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        words = [w.strip() for w in words]
        
        words = [w for w in words if w]
        
        words = [w for w in words if w.isalnum()]
        
        words = [w for w in words if not w.isdigit()]
        
        words = [w for w in words if len(w) > 1]
        
        words = [w for w in words if len(w) == 1]
        
        words = [w for w in words if not w in ['', '