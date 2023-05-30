#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or iterates over a port. """    
    
    # Get the port number or iterate over all ports
    ports = range(1,65535)
    
    # Iterate over all ports
    for port in ports:
        print(port)
        
    # Iterate over all ports until we reach the port
    while True:
        port = input('Enter port number: ')
        if port == ports:
            break
        else:
            print(port)
            
    # Close the port
    port.close()
    
    # Close the port 