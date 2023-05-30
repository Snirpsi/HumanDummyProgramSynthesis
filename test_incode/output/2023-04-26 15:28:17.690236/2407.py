#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    
    ports = Ports(ports_file)
    
    for port in ports:
        port.open()
        port.