#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or opens all ports. """    
    while True:
        ports = find_ports()
        open_ports(ports)
        time.sleep(1)
