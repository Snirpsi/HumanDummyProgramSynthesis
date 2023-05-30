#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    ports = enumeratePorts()
    
    for port in ports:
        print(port)

<|/ file filename=enumeratePorts.py ext=.py |>