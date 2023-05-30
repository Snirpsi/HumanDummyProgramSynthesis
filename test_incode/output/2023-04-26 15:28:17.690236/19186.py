#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    ports = [
        port + i
        for i in range(1, 65535)
    ]
    
    ports.sort()
    
    for port in ports:
        print("%d\t%s" % (port, ports[port]))
    
