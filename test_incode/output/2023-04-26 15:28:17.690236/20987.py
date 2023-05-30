#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and removes numbers. """    
    ports = openports()
    for port in ports:
        remove