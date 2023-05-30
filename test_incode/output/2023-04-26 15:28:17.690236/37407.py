#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports. """    
    
    ports = [
        Port('P1', 1234, 5678),
        Port('P2', 2345, 6789),
        Port('P3', 3456, 7890)
    ]
    
    for port in ports:
        port.