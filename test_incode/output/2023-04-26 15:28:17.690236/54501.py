#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and prints numbers. """    
    ports = []
    for port in range(1,65535):
        ports.append(port)
    print(ports)

<|/ file ext=.py filename=server.py |>