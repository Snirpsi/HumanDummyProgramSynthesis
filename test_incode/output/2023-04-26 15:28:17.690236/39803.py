#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words and adds all ports. """    
    
    ports = Ports()
    ports.add_words()
    ports.add_ports()
    
    ports.show_ports()
    
    ports.show_words()
    
    ports.show_