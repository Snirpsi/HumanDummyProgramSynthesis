#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or converts all ports. """    
    while True:
        
        # Open a port if one isn't already open
        if port is None:
            port = find_port()
            
        # Convert all ports
        convert_ports()
        
        # Sleep for one second
        time.sleep(1)
        
    # Close the port if one was open
    if port is not None:
        port.close()
        
