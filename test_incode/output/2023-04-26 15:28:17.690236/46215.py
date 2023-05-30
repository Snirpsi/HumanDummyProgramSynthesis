#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    ports = find_ports()
    while True:
        for port in ports:
            print(port)
        time.sleep(1)
