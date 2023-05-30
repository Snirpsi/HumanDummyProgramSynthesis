#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or multiplyes all ports. """    
    while True:
        ports = input("Enter ports separated by comma: ").split(",")
        for port in ports:
            print(port*