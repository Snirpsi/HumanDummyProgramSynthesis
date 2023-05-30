#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or returns all ports. """    
    while True:
        ports = find_ports()
        if ports:
            for port in ports:
                