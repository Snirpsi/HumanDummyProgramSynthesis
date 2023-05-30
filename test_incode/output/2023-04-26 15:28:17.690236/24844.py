#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or enumerates all ports. """    
    while True:
        ports = input("Enter ports: ").split()
        for port in ports:
            