#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '/dev/ttyACM0'
    
    