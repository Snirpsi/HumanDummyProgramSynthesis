#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port. """    
    import sys
    port = int(sys.argv[1])
    
    if port == 80:
        print('Port 80')
    elif port == 443:
        print('Port 443')
    elif port == 444:
        print('Port 444')
    elif port == 80