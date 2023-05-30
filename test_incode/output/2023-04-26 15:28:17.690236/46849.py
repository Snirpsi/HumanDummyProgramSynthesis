#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
    
    with open(filename) as f:
        words = [line.strip() for line in f.readlines()]
    
    print(words)
    
