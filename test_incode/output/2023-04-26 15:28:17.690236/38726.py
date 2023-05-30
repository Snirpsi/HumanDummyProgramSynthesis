#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input or opens all ports. """    
    while True:
        ports = input("Enter a port number or press enter to open all ports: ")
        if ports == '':
            ports = 