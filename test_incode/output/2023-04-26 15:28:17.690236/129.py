#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports. """    
    while True:
        ports = find_ports()
        for port in ports:
            print(port)
        time.sleep(1)
