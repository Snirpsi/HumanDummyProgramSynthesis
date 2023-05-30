#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and returns all ports. """    
    ports = find_ports()
    
    ports_str = ''
    for port in ports:
        ports_str += str(port) + ' '
    
    print(ports_str)
    
