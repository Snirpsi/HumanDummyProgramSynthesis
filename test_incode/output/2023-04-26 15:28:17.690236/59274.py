#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and multiplyes all ports. """    
    ports = input("Enter ports separated by spaces ")
    ports = ports.split()
    ports = [int(p) for p in ports]
    ports = [p*2 for p in ports]
    print(ports)
    
