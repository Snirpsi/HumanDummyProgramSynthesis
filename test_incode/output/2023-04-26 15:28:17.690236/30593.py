#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports. """    
    ports = list( openbsd.get_open_ports() )
    for port in ports:
        print( port )
