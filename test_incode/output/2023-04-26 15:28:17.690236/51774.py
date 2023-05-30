#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports and removes a port. """    
    ports = Ports()
    ports.print_ports()
    ports.remove_port('COM1')
    ports.print_ports()
    
