#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and enumerates all ports. """    
    while True:
        ports = enumerate_ports()
        for port in ports:
            print(port)
