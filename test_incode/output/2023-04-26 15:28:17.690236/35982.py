#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    import sys
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '' or line == '\n':
            continue
        
        parts = line.split('\t')
        
        if len(parts) != 2:
            continue
        
        