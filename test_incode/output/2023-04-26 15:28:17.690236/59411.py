#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port. """    
    
    # Get the port
    port = int(sys.argv[1])
    
    # Remove it
    remove_port(port)
    
    # Print the result
    print("Port removed")
    
