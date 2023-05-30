#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or prints a port. """    
    ports = openports()
    for port in ports:
        print(port)
    
