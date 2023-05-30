#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or removes a list of numbers. """    
    
    # Get the list of ports
    ports = sys.argv[1:]
    
    # Remove all ports
    if len(ports) > 0:
        for port in ports:
            remove_port(port)
    else:
        print('No ports specified')
        
