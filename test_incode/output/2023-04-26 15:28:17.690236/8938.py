#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports or removes a port. """    
    
    ports = find_ports()
    
    for port in ports:
        remove_port(port)
        
    print("Done!")
    
