#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of numbers or enumerates a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the list of ports
    ports = [port]
    
    # Iterate over the ports
    for port in ports:
        
        # Get the port number
        port_number = port
        
        # Print the port number
        print('Port #' + str(port_number))
        
        # Print the port name
        print('Port Name: ' + 