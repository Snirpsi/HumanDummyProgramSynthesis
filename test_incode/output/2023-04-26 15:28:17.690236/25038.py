#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input or returns all ports. """    
    ports = enumerate_ports()
    
    for port in ports:
        print('Port {} is {}'.format(port, ports[port]))

<|/ file filename=enumerate_ports.py source=github |>