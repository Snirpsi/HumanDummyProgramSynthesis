#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input and iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    for char in sys.stdin:
        print(char)
        
        if char == '\n':
            break
            
    
