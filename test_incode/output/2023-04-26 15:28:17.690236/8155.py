#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports or prints a list of numbers. """    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
    
    for port in ports:
        print(port)
    
