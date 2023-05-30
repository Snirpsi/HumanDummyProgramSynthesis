#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and prints all ports. """    
    while True:
        ports = []
        for port in range(0, 65535):
            ports.append(port)
        print("