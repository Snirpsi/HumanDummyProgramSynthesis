#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and multiplyes all ports. """    
    while True:
        ports = input("Enter ports to multiply (separated by commas): ")
        ports = ports.split(",")
        for port in ports:
            port = int(port)
            port