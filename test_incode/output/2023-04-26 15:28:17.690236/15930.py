#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and stores all ports. """    
    ports = Ports()
    ports.open()
    ports.close()
    
