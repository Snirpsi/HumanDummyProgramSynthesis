#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    while True:
        ports = find_ports()
        for port in ports:
            process_port(port)
        time.sleep(