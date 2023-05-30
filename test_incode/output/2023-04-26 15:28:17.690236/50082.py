#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or multiplyes all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m ports.ports [ports]")
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        if port < 0:
            print("Port must be positive")
            sys.exit()
        
        ports.