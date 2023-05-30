#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and stores all ports. """    
    ports = []
    for port in range(0,65535):
        ports.append(port)
    print(ports)
