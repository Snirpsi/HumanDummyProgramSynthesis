#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        print(int(sys.argv[1]))
    else:
        print("Usage: python3 