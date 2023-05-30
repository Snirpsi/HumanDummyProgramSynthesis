#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and opens user input. """    
    while True:
        ports = input("Enter the port numbers to close: ")
        ports = ports.split()
        ports = [int(p) for p in ports]
        ports.sort()
        for port in ports:
            