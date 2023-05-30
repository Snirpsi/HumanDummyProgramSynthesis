#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports and enumerates all ports. """    
    ports = enumerate_ports()
    ports_str = str(ports)
    ports_str = ports_str.replace("'", '')
    print(ports_str)
    
