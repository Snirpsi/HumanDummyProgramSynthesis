#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports. """    
    
    ports = []
    
    ports.append( ('tcp', 80, 80) )
    ports.append( ('tcp', 443, 443) )
    
    for port, 