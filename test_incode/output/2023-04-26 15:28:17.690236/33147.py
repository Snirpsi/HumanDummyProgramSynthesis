#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        for line in f:
            print(line.strip())
    
