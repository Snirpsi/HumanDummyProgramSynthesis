#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and converts user input. """    
    
    ports = openPorts()
    
    for port in ports:
        port