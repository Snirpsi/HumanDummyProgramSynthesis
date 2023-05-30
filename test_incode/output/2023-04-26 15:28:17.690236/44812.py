#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or returns all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 9999
    
    while True:
        sys.stdout.write('