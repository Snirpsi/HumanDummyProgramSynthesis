#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or returns all ports. """    
    while True:
        ports = input("Enter ports separated by comma: ").split(',')
        if ports:
            ports = [int(port) for port in ports]
            for port in ports:
                