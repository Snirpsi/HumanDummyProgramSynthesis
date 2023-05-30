#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or adds a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the port number from the config file
    port_number = int(sys.argv[2])
    
    # Add the port to the config file
    config_