#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and iterates over all ports. """    
    
    ports = openPorts()
    
    for port in ports:
        port