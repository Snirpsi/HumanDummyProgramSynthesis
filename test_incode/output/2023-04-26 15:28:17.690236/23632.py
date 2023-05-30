#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
        
    with open(filename) as f:
        for line in f:
            print(line)
            
