#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-numbers.py <file> ")
        sys.exit()
    
    file = sys.argv[1]
    
    with open(file) as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        if line[0].isdigit():
            print(line)
    
