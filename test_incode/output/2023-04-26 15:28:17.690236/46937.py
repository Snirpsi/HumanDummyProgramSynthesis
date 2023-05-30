#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and multiplyes all ports. """    
    port = int(sys.argv[1])
    ports = range(port)
    ports = map(lambda x: x*x, ports)
    print(ports)

<|/ file ext=.py source=github |>