#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports. """    
    
    ports = []
    
    # Open ports
    for port in range(1, 65535):
        ports.append(port)
        
    # Close ports
    for port in ports:
        
        # Open port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to port
        sock.connect(("", port))
        
        # Close port
        sock.close()
        
        # Print port
        print("Port {} is open".format(port))
        
    # Close program
    sys.exit()
    
