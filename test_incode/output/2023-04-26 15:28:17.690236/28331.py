#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or returns all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    # Iterate over all ports
    for port in ports:
        
        # Start a server on port 