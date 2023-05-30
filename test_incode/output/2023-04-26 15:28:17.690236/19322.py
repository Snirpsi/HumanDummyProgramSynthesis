#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and removes a port. """    
    
    ports = input("Enter a list of ports: ")
    
    ports = [int(p) for p in ports.split(',')]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[: