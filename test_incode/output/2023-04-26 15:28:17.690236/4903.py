#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = float(sys.argv[1])
        
        if sys.argv[2] == '*':
            
            number *= 