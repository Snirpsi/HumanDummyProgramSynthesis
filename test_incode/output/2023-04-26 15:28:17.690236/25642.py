#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and converts a list of numbers. """    
    ports = []
    for port in ports:
        port.remove()
    ports = list(set(ports))
    ports.sort()
    ports = [str(port) for port in ports]
    print(ports)
    
