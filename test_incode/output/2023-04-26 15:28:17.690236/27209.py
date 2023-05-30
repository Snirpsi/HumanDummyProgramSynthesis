#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    port = int(port)
    
    ports = range(port, 65535)
    
    for port in ports:
        print(port)
    
