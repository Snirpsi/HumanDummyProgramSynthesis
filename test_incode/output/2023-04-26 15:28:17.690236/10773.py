#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = range(1,65535)
    ports_multiply = []
    for port in ports:
        ports_multiply.append(port*