#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports and removes words. """    
    
    ports = find_ports()
    ports_clean = remove_words(ports)
    
    print(ports_clean)
    
