#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Port {} is open".format(port))
    
