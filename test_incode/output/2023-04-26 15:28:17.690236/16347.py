#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        for word in words:
            
            print(word*