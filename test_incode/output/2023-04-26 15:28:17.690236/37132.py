#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 open_input.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        lines = f.readlines()
    
    for line in lines:
        print(line)
        
    
