#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or prints a list of words. """    
    ports = find_ports()
    for port in ports:
        print(port)
        
