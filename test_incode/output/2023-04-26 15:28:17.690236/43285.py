#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports and stores all ports. """    
    while True:
        ports = find_ports()
        store_ports(ports)
        time.sleep(60)
