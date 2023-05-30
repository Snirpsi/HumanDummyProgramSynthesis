#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports or converts user input. """    
    
    ports = []
    
    # Iterate over all ports
    for port in ports:
        # Convert user input to integer
        port = int(port)
        
        # Check if port is valid
        if port < 0 or port > 65535:
            print('Invalid port number!')
        else:
            # Add port to list
            ports.append(port)
            
    # Print list
    print('Ports:', ports)
    
