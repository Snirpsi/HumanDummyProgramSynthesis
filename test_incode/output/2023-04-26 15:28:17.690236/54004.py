#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or calculates all ports. """    
    port = int(sys.argv[1])
    ports = range(port)
    ports_