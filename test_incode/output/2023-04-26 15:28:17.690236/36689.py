#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port and multiplyes all ports. """    
    ports = input("Enter the ports separated by comma: ")
    ports = ports.split(",")
    for port in ports:
        port = int(port)
        port