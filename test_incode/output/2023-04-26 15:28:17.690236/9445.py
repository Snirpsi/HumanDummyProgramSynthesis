#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or enumerates all ports. """    
    ports = []
    
    # Open a port if one isn't already open
    try:
        port = int(sys.argv[1])
        ports.append(port)
    except:
        ports = range(1024)
    
    # Print all ports
    for port in ports:
        print(port)
        
    # Print all ports 