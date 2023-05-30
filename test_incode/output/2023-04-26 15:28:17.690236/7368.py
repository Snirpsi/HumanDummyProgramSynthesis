#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create the port
    port = Port(port)
    
    # Add the port
    port.add()
    
    # Print the port
    print(port)
    
    # Print the port list
    print(port.list)
    
    # Print the port info
    print(port.info)
    
    # Print the port infos
    print(port.infos)
    
    # Print the port infos
    print(port.info