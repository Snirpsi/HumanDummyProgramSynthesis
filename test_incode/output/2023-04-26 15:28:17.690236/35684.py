#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and converts all ports. """    
    while True:
        ports = input("Enter ports: ")
        ports = ports.split()
        ports = ports + ["