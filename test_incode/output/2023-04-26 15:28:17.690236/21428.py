#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words or opens all ports. """    
    ports = listen_ports()
    
    # Open the ports
    for port in ports:
        open_port(port)
    
    # Return the list of words or open all ports
    return ports
    
