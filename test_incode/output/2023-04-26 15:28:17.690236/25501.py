#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or opens all ports. """    
    while True:
        ports = listen_ports()
        
        for port in ports:
            