#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or multiplyes user input. """    
    ports = input("Enter ports: ")
    ports = ports.split()
    ports = [int(port) for port in ports]
    ports = ports * 2
    print(ports)
