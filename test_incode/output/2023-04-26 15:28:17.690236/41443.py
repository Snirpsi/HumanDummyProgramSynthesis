#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
        
    print("Port 