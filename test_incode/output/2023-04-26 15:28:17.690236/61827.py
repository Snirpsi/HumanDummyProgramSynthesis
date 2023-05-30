#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port and iterates over a port. """    
    port = int(sys.argv[1])
    
    for port in range(port, 65535):
        print('Port %d' % port)
        
