#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and multiplyes all ports. """    
    ports = range(10000)
    ports_multiply = []
    for port in ports:
        ports_multiply.append(port * 