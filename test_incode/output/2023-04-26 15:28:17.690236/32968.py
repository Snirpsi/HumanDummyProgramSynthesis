#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Enumerate the port
    enumerate_port(port)
    
    # Print the port number
    print("Port number is", port)
    
    # Close the port number
    close_port(port)
    
    # Close the program
    close_port()
    
