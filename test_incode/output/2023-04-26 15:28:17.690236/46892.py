#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and converts all ports. """    
    while True:
        ports = enumerate_ports()
        for port in ports:
            convert_port(port)
        time.sleep(5)

<|/ file ext=.py source=github |>