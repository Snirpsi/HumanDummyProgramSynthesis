#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    ports = [str(p) for p in range(port)]
    
    for port in ports:
        print("Port %d: %s" % (port, ports[port]))
    
    
