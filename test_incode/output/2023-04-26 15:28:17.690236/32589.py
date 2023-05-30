#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or removes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        words = [w.strip() for w in words]
        
        words = [w for w in words if w]
        
        words = [w for w in words if not w.isdigit()]
        
        words = [w for w in words if not w.isalpha()]
        
        words = [w for w in words if not w in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for w in words if w not in [' ', '\n']]
        
        words = [w for 