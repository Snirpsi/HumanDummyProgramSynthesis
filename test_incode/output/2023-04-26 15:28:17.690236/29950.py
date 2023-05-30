#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports. """    
    ports = []
    
    for port in get_ports():
        ports.append(port)
        
    print('\n'.join(ports))
    
