#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports. """    
    ports = Ports()
    while True:
        ports.update()
        ports.