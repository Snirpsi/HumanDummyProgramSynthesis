#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <ports>" % sys.argv[0])
        sys.exit(1)
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        