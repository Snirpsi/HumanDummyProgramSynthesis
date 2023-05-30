#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        line = sys.argv[1]
        
        print(line)
    
    else:
        print("No input given.")
        
    
