#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and adds all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    for port in range(port, 65535):
        ports.append(port)
    
    for port in ports:
        print("Port %