#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and multiplyes numbers. """    
    ports = [
        int(port) for port in sys.argv[1:]
    ]
    ports = [port * n for n, port in enumerate(ports)]
    print(ports)

<|/ file source=github ext=.py |>