#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or converts words. """    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        sys.stdout.write("Port %d: %s\n" % (port, ports[port]))
        
    
