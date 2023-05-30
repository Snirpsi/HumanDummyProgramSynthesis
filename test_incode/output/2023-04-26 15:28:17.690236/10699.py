#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and returns all ports. """    
    ports = []
    for port in range(1,65535):
        ports.append(port)
    print(ports)
    
