#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        for arg in sys.argv[1:]:
            
            print(arg)
            
    else:
        
        print("No arguments given.")
        
