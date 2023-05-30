#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or returns a port. """    
    while True:
        ports = find_ports()
        if ports:
            for port in ports:
                print(port)
        else:
            break
            
