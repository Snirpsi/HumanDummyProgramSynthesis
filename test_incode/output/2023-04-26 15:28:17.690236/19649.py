#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and converts all ports. """    
    ports = sys.argv[1:]
    ports = ports.split(',')
    for port in ports:
        port = int(port)
        convert_port(port)
<|/ file ext=.py source=github |>