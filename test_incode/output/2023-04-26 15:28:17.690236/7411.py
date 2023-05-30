#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and adds all ports. """    
    while True:
        ports = input('Enter ports: ')
        ports = ports.split()
        for port in ports:
            port = int(port)
            ports.append(port)
        print('Ports:', ports)
        ports_