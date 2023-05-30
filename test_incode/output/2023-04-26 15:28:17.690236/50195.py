#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and converts a port. """    
    ports = enumerate_ports()
    ports_string = ""
    for port in ports:
        ports_string += str(port) + " "
    print(ports_string)
    
