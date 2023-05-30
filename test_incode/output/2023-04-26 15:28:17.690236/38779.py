#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or removes all ports. """    
    ports = enumeratePorts()
    for port in ports:
        removePort(port)
    
