#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or iterates over a port. """    
    while True:
        ports = find_ports()
        for port in ports:
            print_port(port)
        time.sleep(1)
