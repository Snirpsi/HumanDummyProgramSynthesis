#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or multiplyes a list of numbers. """    
    ports = input("Enter a list of ports separated by spaces (no spaces!): ")
    ports = ports.split()
    ports = [int(p) for p in ports]
    ports = [p*2 for p in ports]
    print(ports)
