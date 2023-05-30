#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    port = '/dev/ttyUSB0'
    ports = enumeratePort(port)
    for p in ports:
        print(p)

<|/ file filename=enumerate.py ext=.py |>