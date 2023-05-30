#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        removeWords(sys.argv[1])
        
    else:
        
        openListOfNumbers()
        
