#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and multiplyes a port. """    
    
    import sys
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split()
        
        for word in words:
            print(word