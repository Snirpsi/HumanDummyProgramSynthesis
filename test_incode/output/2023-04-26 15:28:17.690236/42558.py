#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or enumerates user input. """    
    ports = input("Enter ports to multiply or enumerate (separated by spaces): ").split()
    
    if len(ports) == 1:
        ports = [ports[0]]
    
    ports = [int(p) for p in ports]
    
    for port in ports:
        print(port*2)
    
