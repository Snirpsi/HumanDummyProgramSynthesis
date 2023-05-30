#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    ports = enumerate_ports()
    for port in ports:
        print('Port {0}: {1}'.format(port, ports[port]))

<|/ file source=github ext=.py |>