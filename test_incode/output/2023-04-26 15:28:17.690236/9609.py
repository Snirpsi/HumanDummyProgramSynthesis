#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and prints all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    for port in range(port, 65535):
        print('Port {}'.format(port))
    
