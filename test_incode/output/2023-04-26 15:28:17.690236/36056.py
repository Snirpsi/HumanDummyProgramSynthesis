#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores all ports. """    
    
    ports = Ports()
    ports.load_ports()
    
    ports.save_ports()
    
    ports.print_ports()
    
    ports.print_ports_