#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or multiplyes all ports. """    
    while True:
        fruits = input("Enter fruits: ")
        ports = input("Enter ports: ")
        ports = ports.split()
        ports = [int(i) for i in ports]
        ports = [x*