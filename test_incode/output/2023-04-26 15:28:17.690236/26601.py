#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and prints fruits. """    
    ports = openports()
    for port in ports:
        fruit = openfru