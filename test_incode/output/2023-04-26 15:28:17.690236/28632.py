#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports or adds words. """    
    while True:
        ports = input("Enter ports: ")
        ports = ports.split()
        ports = [int(p) for p in ports]
        ports = sum(ports)
        print(ports)
        
