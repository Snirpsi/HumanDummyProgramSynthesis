#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port and returns a list of numbers. """    
    ports = []
    with open('/dev/ttyUSB0','rb') as port:
        ports.append(port.read())
    return ports

<|/ file source=github filename=