#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or enumerates all ports. """    
    ports = input("Enter a port number: ")
    ports = ports.split()
    ports = [int(p) for p in ports]
    ports.sort()
    print("Ports:", ports)
    
