#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Remove that port
    remove_port(port)
    
    # Print the new port
    print("Port removed: " + port)
    
