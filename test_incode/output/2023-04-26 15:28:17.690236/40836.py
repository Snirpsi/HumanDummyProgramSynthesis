#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python print-numbers.py <filename>")
        sys.exit()
    
    with open(sys.argv[1]) as f:
        for line in f:
            print(line)
    
