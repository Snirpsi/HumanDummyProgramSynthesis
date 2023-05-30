#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or enumerates user input. """    
    while True:
        ports = input("Enter ports separated by comma: ")
        ports = ports.split(',')
        for port in ports:
            port = int(port)
            