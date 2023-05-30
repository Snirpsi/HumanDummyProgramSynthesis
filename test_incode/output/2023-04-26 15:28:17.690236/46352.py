#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and removes a list of numbers. """    
    ports = openports()
    ports.remove('1234')
    ports.remove('1234