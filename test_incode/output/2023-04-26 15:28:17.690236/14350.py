#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and removes all ports. """    
    
    ports = input("Enter the ports to remove: ")
    ports = ports.split()
    
    for port in ports:
        