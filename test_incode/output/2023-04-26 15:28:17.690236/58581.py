#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = input("Enter a port number: ")
    
    