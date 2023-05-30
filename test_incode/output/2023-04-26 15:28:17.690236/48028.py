#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input and iterates over all ports. """    
    ports = input("Enter ports: ")
    ports = ports.split(",")
    ports = list(map(int, ports))
    
    ports_multiplied = 0
    for port in ports:
        ports_multiplied += port * 