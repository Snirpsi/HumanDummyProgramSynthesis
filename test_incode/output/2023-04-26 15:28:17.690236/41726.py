#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and iterates over all ports. """    
    ports = input("Enter ports: ")
    ports = ports.split()
    ports = [int(p) for p in ports]
    
    while True:
        ports_multiplied = []
        for port in ports:
            ports_multiplied.append(port * 2)
        
        print(ports_multiplied)
        
        ports = input("Enter ports: ")
        ports = ports.split()
        ports = [int(p) for p in ports]
        
