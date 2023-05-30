#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == '--help':
            
            print('Usage: python number