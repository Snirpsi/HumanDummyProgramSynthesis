#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or converts a port. """    
    import sys
    port = int(sys.argv[1])
    
    # Convert port to string and print it
    port_str = str(port)
    print(port_str)
    
    # Iterate over all ports and print them
    for port in range(1, 65535):
        port_str = str(port)
        print(port_str)
        
    # Iterate over all ports and print them in reverse order
    for port in range(65536, 