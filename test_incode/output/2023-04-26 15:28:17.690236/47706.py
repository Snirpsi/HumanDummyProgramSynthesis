#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers and converts a port. """    
    
    ports = [int(i) for i in input("Enter a port number: ").split()]
    
    ports_converted = [ports[0]]
    
    for port in ports[1:]:
        ports_converted.append(port*ports_converted[-1]