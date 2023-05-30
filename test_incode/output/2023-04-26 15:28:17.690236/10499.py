#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    # Get the arguments
    args = sys.argv[1:]
    
    # Get the ports to remove
    ports = args[0]
    
    # Remove them
    remove_ports(ports)
    
    # Print a message
    print('Removed ports:')
    
    # Print the ports
    for port in ports:
        print('\t{}'.format(port))
    
