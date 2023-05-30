#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports or multiplyes a list of numbers. """    
    while True:
        ports = input("Enter ports: ")
        ports = ports.split()
        ports = [int(p) for p in ports]
        ports = ports * len(ports)
        print(ports)
        
