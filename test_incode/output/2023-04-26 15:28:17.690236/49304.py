#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python ports.py <port>")
        sys.exit()
    
    port = sys.argv[1]
    
    ports = ports.ports(port)
    
    for port in ports:
        print(port)
    
