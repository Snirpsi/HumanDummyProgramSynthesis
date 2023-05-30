#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port. """    
    
    # Get the arguments from the command line
    args = sys.argv[1:]
    
    # Get the port number
    port = int(args[0])
    
    # Get the port
    port = Port(port)
    
    # Add the port
    port.add()
    
    # Print the port
    print(port)
    
    # Print the ports
    for port in port.ports:
        print(port)
    
    # Print the ports 