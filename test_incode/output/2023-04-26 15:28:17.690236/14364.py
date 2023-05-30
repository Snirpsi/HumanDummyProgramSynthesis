#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and adds a list of numbers. """    
    ports = input("Enter a list of ports: ")
    ports = ports.split()
    ports = list(filter(None, ports))
    ports = list(map(int, ports))
    ports.sort()
    ports = list(map(str, ports))
    ports = ports[: