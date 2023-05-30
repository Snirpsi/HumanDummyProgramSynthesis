#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input and removes all ports. """    
    ports = input("Enter the ports you want to remove: ")
    ports = ports.split()
    ports = list(filter(None, ports))
    ports = " ".join(ports)
    print(ports)
    
