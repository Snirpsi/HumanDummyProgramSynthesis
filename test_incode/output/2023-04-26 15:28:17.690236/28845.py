#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and enumerates fruits. """    
    while True:
        ports = enumerate_ports()
        fruits = enumerate_fruits(ports)
        for fruit in fruits:
            print(