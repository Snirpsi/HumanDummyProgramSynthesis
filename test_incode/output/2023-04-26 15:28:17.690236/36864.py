#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python input.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        for line in f:
            print(line)
            
