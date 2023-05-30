#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    import sys
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        line = line.split('\t')
        
        if len(line) != 2:
            continue
        
        