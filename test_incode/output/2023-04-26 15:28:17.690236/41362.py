#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input or converts all ports. """    
    ports = input("Enter ports: ")
    ports = ports.split()
    ports = list(map(int, ports))
    ports = list(set(ports))
    ports.sort()
    ports = list(map(str, ports))
    ports = ports[: