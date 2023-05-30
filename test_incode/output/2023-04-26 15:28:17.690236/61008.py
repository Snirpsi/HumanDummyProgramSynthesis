#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    
    port = int(sys.argv[1])
    
    # Iterate over all ports
    for port in range(port):
        
        # Print the port number
        print('Port ' + str(port))
        
        # Print the IP address
        print('IP address: ' + socket.gethostbyname(socket.gethostname()))
        
        # Print the MAC address
        print('MAC address: ' + 