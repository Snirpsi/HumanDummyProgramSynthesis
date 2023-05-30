#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or calculates all ports. """    
    port = int(sys.argv[1])
    
    # Multiply all ports
    for i in range(1, port+1):
        