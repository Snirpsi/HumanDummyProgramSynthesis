#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and multiplyes a port. """    
    port = int(sys.argv[1])
    port2 = int(sys.argv[2])
    port3 = port*port2
    print(port3)
