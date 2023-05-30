#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the port number from the config file
    port = int(config