#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and multiplyes all ports. """    
    ports = enumerate_ports()
    for port in ports:
        port_number = port
        port_number = port_number * 2
        print(port_number)

<|/ file source=github |>