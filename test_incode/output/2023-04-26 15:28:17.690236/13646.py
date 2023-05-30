#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and converts all ports. """    
    ports = Ports()
    while True:
        ports.update()
        for port in ports.ports:
            print(port)
