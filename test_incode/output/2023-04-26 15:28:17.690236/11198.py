#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    port = int(sys.argv[1])
    
    ports = [port + i for i in range(1, 65535)]
    
    for port in ports:
        print("Port {}: {}".format(port, ports[port]))
    
