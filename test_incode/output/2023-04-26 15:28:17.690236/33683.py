#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port or opens a port. """    
    port = None
    
    # Open a port if none is given
    if len(sys.argv) == 1:
        port = openport()
    else:
        port = sys.argv[1]
    
    # Store the port in a file
    storeport(port)
    
    # Close the port
    closeport(port)
    
