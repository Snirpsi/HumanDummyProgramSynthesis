#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and calculates a list of words. """    
    ports = Ports()
    ports.remove_all_ports()
    ports.calculate_words()
    ports.print_words()
    
    
