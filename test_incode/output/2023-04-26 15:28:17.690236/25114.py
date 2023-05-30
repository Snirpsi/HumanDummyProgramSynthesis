#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words. """    
    import sys
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            print(line)
        else:
            break
    
