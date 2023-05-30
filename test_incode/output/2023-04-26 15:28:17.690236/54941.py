#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 input.py <filename>")
        exit(1)
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        lines = f.readlines()
    
    for line in lines:
        print(line)
        
