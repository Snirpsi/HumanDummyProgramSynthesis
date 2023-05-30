#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and stores all ports. """    
    ports = Ports()
    while True:
        ports.add_port()
        ports.store_ports()
        time.sleep(10)
