#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter the file name: ")
    
    with open(filename) as f:
        words = f.read().split()
    
    print(words)
    
